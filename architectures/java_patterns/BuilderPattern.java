/**
 * Gang of Four: Builder Creational Pattern in Java.
 * Fluent API for constructing immutable domain entities.
 */

class HttpRequest {
    private final String url;
    private final String method;
    private final String body;
    private final int timeoutMs;

    private HttpRequest(Builder builder) {
        this.url = builder.url;
        this.method = builder.method;
        this.body = builder.body;
        this.timeoutMs = builder.timeoutMs;
    }

    public String getUrl() { return url; }
    public String getMethod() { return method; }
    public String getBody() { return body; }
    public int getTimeoutMs() { return timeoutMs; }

    public static class Builder {
        private String url;
        private String method = "GET";
        private String body = "";
        private int timeoutMs = 5000;

        public Builder url(String url) {
            this.url = url;
            return this;
        }

        public Builder method(String method) {
            this.method = method;
            return this;
        }

        public Builder body(String body) {
            this.body = body;
            return this;
        }

        public Builder timeoutMs(int timeoutMs) {
            this.timeoutMs = timeoutMs;
            return this;
        }

        public HttpRequest build() {
            if (url == null || url.isEmpty()) {
                throw new IllegalStateException("URL is mandatory");
            }
            return new HttpRequest(this);
        }
    }
}

public class BuilderPattern {
    public static void main(String[] args) {
        HttpRequest req = new HttpRequest.Builder()
            .url("https://api.github.com/repos/igor-kan/codes")
            .method("POST")
            .body("{\"name\":\"test\"}")
            .timeoutMs(10000)
            .build();

        assert req.getUrl().contains("igor-kan");
        assert "POST".equals(req.getMethod());
        assert req.getTimeoutMs() == 10000;

        System.out.println("[Java Patterns] Builder pattern verified.");
    }
}
