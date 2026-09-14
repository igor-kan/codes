// Lazy-loading images when they enter the viewport.
export function lazyLoadImages(selector = "img[data-src]") {
  const observer = new IntersectionObserver(
    (entries, obs) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        const img = entry.target;
        img.src = img.dataset.src;
        img.removeAttribute("data-src");
        obs.unobserve(img);
      }
    },
    { rootMargin: "200px" },
  );

  document.querySelectorAll(selector).forEach((img) => observer.observe(img));
  return observer;
}
