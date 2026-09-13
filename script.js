(() => {
  const doc = document.documentElement;
  const header = document.querySelector(".site-header");
  const nav = document.getElementById("primary-nav");
  const menuToggle = document.getElementById("menu-toggle");
  const langToggle = document.getElementById("lang-toggle");
  const progress = document.getElementById("scroll-progress");
  const toTop = document.getElementById("to-top");
  const navLinks = nav ? [...nav.querySelectorAll("a[href^='#']")] : [];
  const sections = navLinks
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  const titles = {
    ar: "الموسى للتقنية وخدمات الأنظمة الأمنية | Al-Mousa Technology",
    en: "Al-Mousa for Technology and Security Systems | Corporate Profile",
  };

  const descriptions = {
    ar: "شركة الموسى للتقنية وخدمات الأنظمة الأمنية — حلول أمنية وتقنية متكاملة في الرياض، المملكة العربية السعودية.",
    en: "Al-Mousa for Technology and Security Systems Services Co. — integrated security and technology solutions in Riyadh, Kingdom of Saudi Arabia.",
  };

  function setLanguage(lang) {
    const next = lang === "en" ? "en" : "ar";
    doc.lang = next;
    doc.dir = next === "ar" ? "rtl" : "ltr";
    document.title = titles[next];
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.setAttribute("content", descriptions[next]);
    localStorage.setItem("al-mousa-lang", next);
    const url = new URL(window.location.href);
    if (next === "en") url.searchParams.set("lang", "en");
    else url.searchParams.delete("lang");
    history.replaceState({}, "", url);
  }

  function initLanguage() {
    const params = new URLSearchParams(window.location.search);
    const fromQuery = params.get("lang");
    const stored = localStorage.getItem("al-mousa-lang");
    const preferred =
      fromQuery === "en" || fromQuery === "ar"
        ? fromQuery
        : stored === "en" || stored === "ar"
          ? stored
          : "ar";
    setLanguage(preferred);
  }

  langToggle?.addEventListener("click", () => {
    setLanguage(doc.lang === "ar" ? "en" : "ar");
  });

  menuToggle?.addEventListener("click", () => {
    const open = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!open));
    nav?.classList.toggle("is-open", !open);
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      menuToggle?.setAttribute("aria-expanded", "false");
      nav?.classList.remove("is-open");
    });
  });

  function onScroll() {
    const scrollTop = window.scrollY || doc.scrollTop;
    const height = doc.scrollHeight - doc.clientHeight;
    const ratio = height > 0 ? (scrollTop / height) * 100 : 0;
    if (progress) progress.style.width = `${ratio}%`;
    header?.classList.toggle("is-scrolled", scrollTop > 12);
    toTop?.classList.toggle("is-visible", scrollTop > 520);

    let currentId = "";
    sections.forEach((section) => {
      const top = section.offsetTop - 120;
      if (scrollTop >= top) currentId = `#${section.id}`;
    });
    navLinks.forEach((link) => {
      link.classList.toggle("is-active", link.getAttribute("href") === currentId);
    });
  }

  toTop?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  /* Reveal on scroll */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-in");
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    revealEls.forEach((el) => revealObserver.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("is-in"));
  }

  /* Lazy-load decorative project visuals (content-visibility + deferred paint) */
  const lazyVisuals = document.querySelectorAll(".project__visual");
  if ("IntersectionObserver" in window) {
    const lazyObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-loaded");
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "120px 0px" }
    );
    lazyVisuals.forEach((el) => lazyObserver.observe(el));
  }

  /* Native lazy images fallback enhancement */
  document.querySelectorAll('img[loading="lazy"]').forEach((img) => {
    if (img.complete) return;
    img.addEventListener("load", () => img.classList.add("is-loaded"), { once: true });
  });

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  initLanguage();
  onScroll();

  /* Hero entrance */
  requestAnimationFrame(() => {
    document.querySelector(".hero__content")?.classList.add("is-in");
  });
})();
