(() => {
  const doc = document.documentElement;
  const header = document.querySelector(".site-header");
  const nav = document.getElementById("primary-nav");
  const menuToggle = document.getElementById("menu-toggle");
  const langToggle = document.getElementById("lang-toggle");
  const progress = document.getElementById("scroll-progress");
  const toTop = document.getElementById("to-top");

  const titleAr = document.querySelector('meta[name="title-ar"]')?.content;
  const titleEn = document.querySelector('meta[name="title-en"]')?.content;

  function setLanguage(lang) {
    const next = lang === "en" ? "en" : "ar";
    doc.lang = next;
    doc.dir = next === "ar" ? "rtl" : "ltr";
    if (next === "ar" && titleAr) document.title = titleAr;
    if (next === "en" && titleEn) document.title = titleEn;
    localStorage.setItem("mts-lang", next);
    const url = new URL(location.href);
    if (next === "en") url.searchParams.set("lang", "en");
    else url.searchParams.delete("lang");
    history.replaceState({}, "", url);
  }

  const q = new URLSearchParams(location.search).get("lang");
  const stored = localStorage.getItem("mts-lang");
  setLanguage(q === "en" || q === "ar" ? q : stored === "en" || stored === "ar" ? stored : "ar");

  langToggle?.addEventListener("click", () => setLanguage(doc.lang === "ar" ? "en" : "ar"));
  menuToggle?.addEventListener("click", () => {
    const open = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!open));
    nav?.classList.toggle("is-open", !open);
  });
  nav?.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      menuToggle?.setAttribute("aria-expanded", "false");
      nav.classList.remove("is-open");
    })
  );

  const file = (location.pathname.split("/").pop() || "index.html") || "index.html";
  nav?.querySelectorAll("a").forEach((a) => {
    const href = a.getAttribute("href") || "";
    if (href === file || (file === "" && href === "index.html")) a.classList.add("is-active");
  });

  function onScroll() {
    const y = window.scrollY || doc.scrollTop;
    const h = doc.scrollHeight - doc.clientHeight;
    if (progress) progress.style.width = `${h > 0 ? (y / h) * 100 : 0}%`;
    header?.classList.toggle("is-scrolled", y > 10);
    toTop?.classList.toggle("is-visible", y > 500);
  }
  toTop?.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));

  const reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((e) => {
          if (!e.isIntersecting) return;
          e.target.classList.add("is-in");
          obs.unobserve(e.target);
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -6% 0px" }
    );
    reveals.forEach((el) => io.observe(el));
  } else reveals.forEach((el) => el.classList.add("is-in"));

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
})();
