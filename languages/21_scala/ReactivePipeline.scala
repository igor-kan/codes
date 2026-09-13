/**
 * Functional Reactive Pipeline using Immutable Case Classes and Futures.
 * 
 * Why Scala for this module?
 * Scala seamlessly marries Object-Oriented polymorphism with Pure Functional Programming,
 * monads, and pattern matching, forming the backbone of Apache Spark and Big Data pipelines.
 */

package polyglot.functional

import scala.concurrent.{Future, ExecutionContext}
import scala.util.{Success, Failure}

case class FinancialTick(symbol: String, price: Double, volume: Long)

object ReactivePipeline {
  implicit val ec: ExecutionContext = ExecutionContext.global

  def computeVWAP(ticks: Seq[FinancialTick]): Double = {
    val (totalValue, totalVolume) = ticks.foldLeft((0.0, 0L)) {
      case ((accVal, accVol), tick) =>
        (accVal + tick.price * tick.volume, accVol + tick.volume)
    }
    if (totalVolume > 0) totalValue / totalVolume else 0.0
  }

  def processAsync(ticks: Seq[FinancialTick]): Future[Double] = Future {
    computeVWAP(ticks)
  }

  def main(args: Array[String]): Unit = {
    val sample = Seq(
      FinancialTick("AAPL", 150.0, 100),
      FinancialTick("AAPL", 152.0, 200),
      FinancialTick("AAPL", 149.0, 150)
    )
    val vwap = computeVWAP(sample)
    println(f"Scala Functional VWAP: $vwap%.2f")
  }
}
