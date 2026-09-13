/**
 * Kotlin Coroutines SharedFlow Reactive Event Pipeline.
 * 
 * Why Kotlin for this module?
 * Structured concurrency, lightweight suspension points, and zero-allocation
 * SharedFlow with backpressure buffer strategies make Kotlin the premier modern JVM reactive platform.
 */

package polyglot.reactive

import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

data class MetricEvent(val timestamp: Long, val symbol: String, val price: Double)

class MarketDataPipeline(private val scope: CoroutineScope) {
    private val _events = MutableSharedFlow<MetricEvent>(
        replay = 0,
        extraBufferCapacity = 64,
        onBufferOverflow = BufferOverflow.DROP_OLDEST
    )
    val events: SharedFlow<MetricEvent> = _events.asSharedFlow()

    suspend fun publish(event: MetricEvent) {
        _events.emit(event)
    }

    fun startAnomalyDetector(threshold: Double): Job {
        return scope.launch(Dispatchers.Default) {
            events.filter { it.price > threshold }
                .collect { anomaly ->
                    println("Alert: High price detected on ${anomaly.symbol}: $${anomaly.price}")
                }
        }
    }
}

fun main() = runBlocking {
    val pipeline = MarketDataPipeline(this)
    val detector = pipeline.startAnomalyDetector(100.0)

    pipeline.publish(MetricEvent(System.currentTimeMillis(), "AAPL", 95.0))
    pipeline.publish(MetricEvent(System.currentTimeMillis(), "NVDA", 145.0))

    delay(100)
    detector.cancel()
    println("Kotlin Coroutines Reactive Pipeline execution completed.")
}
