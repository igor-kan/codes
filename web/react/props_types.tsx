// Typing component props, including children and defaults.
import type { ReactNode } from "react";

interface CardProps {
  title: string;
  children?: ReactNode;
  tone?: "neutral" | "danger";
  onSelect?: (title: string) => void;
}

export function Card({ title, children, tone = "neutral", onSelect }: CardProps) {
  return (
    <article className={`card card--${tone}`} onClick={() => onSelect?.(title)}>
      <h2>{title}</h2>
      <div>{children}</div>
    </article>
  );
}
