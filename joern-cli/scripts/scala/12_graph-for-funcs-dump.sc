import scala.jdk.CollectionConverters._

import io.circe.syntax._
import io.circe.generic.semiauto._
import io.circe.{Encoder, Json}
import java.io.{PrintWriter, File => JFile}

import io.shiftleft.semanticcpg.language.types.expressions.generalizations.CfgNode
import io.shiftleft.codepropertygraph.generated.EdgeTypes
import io.shiftleft.codepropertygraph.generated.NodeTypes
import io.shiftleft.codepropertygraph.generated.nodes
import io.shiftleft.dataflowengineoss.language._
import io.shiftleft.semanticcpg.language._
import io.shiftleft.semanticcpg.language.types.expressions.Call
import io.shiftleft.semanticcpg.language.types.structure.Local
import io.shiftleft.codepropertygraph.generated.nodes.MethodParameterIn

import gremlin.scala._
import org.apache.tinkerpop.gremlin.structure.Edge
import org.apache.tinkerpop.gremlin.structure.VertexProperty

final case class GraphForFuncsFunction(function: String,
                                       id: String,
                                       AST: List[nodes.AstNode],
                                       CFG: List[nodes.AstNode],
                                       PDG: List[nodes.AstNode])
final case class GraphForFuncsResult(functions: List[GraphForFuncsFunction])

implicit val encodeEdge: Encoder[Edge] =
  (edge: Edge) =>
    Json.obj(
      ("id", Json.fromString(edge.toString)),
      ("in", Json.fromString(edge.inVertex().toString)),
      ("out", Json.fromString(edge.outVertex().toString))
    )

implicit val encodeNode: Encoder[nodes.AstNode] =
  (node: nodes.AstNode) =>
    Json.obj(
      ("id", Json.fromString(node.toString)),
      ("edges",
        Json.fromValues((node.inE("AST", "CFG").l ++ node.outE("AST", "CFG").l).map(_.asJson))),
      ("properties", Json.fromValues(node.properties().asScala.toList.map { p: VertexProperty[_] =>
        Json.obj(
          ("key", Json.fromString(p.key())),
          ("value", Json.fromString(p.value().toString))
        )
      }))
    )

implicit val encodeFuncFunction: Encoder[GraphForFuncsFunction] = deriveEncoder
implicit val encodeFuncResult: Encoder[GraphForFuncsResult] = deriveEncoder

@main def main(): Unit = {
  val writer = new PrintWriter(new JFile("data/json/12.json"))
  val jsons = GraphForFuncsResult(
    cpg.method.map { method =>
      val methodName = method.fullName
      val methodId = method.toString
      val methodVertex: Vertex = method //TODO MP drop as soon as we have the remainder of the below in ODB graph api

      val astChildren = method.astMinusRoot.l
      val cfgChildren = method.out(EdgeTypes.CONTAINS).asScala.collect { case node: nodes.CfgNode => node }.toList

      val local = new NodeSteps(
        methodVertex
          .out(EdgeTypes.CONTAINS)
          .hasLabel(NodeTypes.BLOCK)
          .out(EdgeTypes.AST)
          .hasLabel(NodeTypes.LOCAL)
          .cast[nodes.Local])
      val sink = local.evalType(".*").referencingIdentifiers.dedup
      val source = new NodeSteps(methodVertex.out(EdgeTypes.CONTAINS).hasLabel(NodeTypes.CALL).cast[nodes.Call]).nameNot("<operator>.*").dedup

      val pdgChildren = sink
        .reachableByFlows(source)
        .l
        .flatMap { path =>
          path.elements
            .map {
              case trackingPoint @ (_: MethodParameterIn) => trackingPoint.start.method.head
              case trackingPoint                          => trackingPoint.cfgNode
            }
        }
        .filter(_.toString != methodId)

      GraphForFuncsFunction(methodName, methodId, astChildren, cfgChildren, pdgChildren.distinct)
    }.l
  ).asJson.toString
  writer.write(jsons)
  writer.close()
}
