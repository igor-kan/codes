FROM golang:1.23 AS build
WORKDIR /src
COPY . .
RUN go test ./... && \
    CGO_ENABLED=0 go build -trimpath -o /app ./cmd/app

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /app /app
EXPOSE 8080
ENTRYPOINT ["/app"]
