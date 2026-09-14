// Error boundaries catch render errors in the subtree.
import { Component } from "react";

export class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { error: null };
  }

  static getDerivedStateFromError(error) {
    return { error };
  }

  componentDidCatch(error, info) {
    console.error("Render error", error, info.componentStack);
  }

  render() {
    if (this.state.error) {
      return this.props.fallback ?? <p role="alert">Something went wrong.</p>;
    }
    return this.props.children;
  }
}
