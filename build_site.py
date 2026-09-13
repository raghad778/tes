#!/usr/bin/env python3
"""Generate Al-Mousa MTS multi-page bilingual website."""
from pathlib import Path

ROOT = Path("/workspace")

NAV = [
    ("index.html", "الرئيسية", "Home"),
    ("about.html", "من نحن", "About"),
    ("vision.html", "الرؤية", "Vision"),
    ("goals.html", "الأهداف", "Goals"),
    ("methodology.html", "المنهجية", "Method"),
    ("services.html", "الخدمات", "Services"),
    ("ecosystem.html", "المنظومة", "Ecosystem"),
    ("why-us.html", "لماذا نحن", "Why Us"),
    ("partners.html", "الشركاء", "Partners"),
    ("projects.html", "المشاريع", "Projects"),
    ("contact.html", "تواصل", "Contact"),
]


def chrome_header(active: str) -> str:
    links = []
    for href, ar, en in NAV:
        cls = ' class="is-active"' if href == active else ""
        links.append(
            f'<a href="{href}"{cls}><span class="lang-ar">{ar}</span><span class="lang-en">{en}</span></a>'
        )
    nav = "\n          ".join(links)
    return f"""  <div class="progress" id="scroll-progress" aria-hidden="true"></div>
  <header class="site-header">
    <div class="nav-shell">
      <a class="brand" href="index.html">
        <img src="assets/brand/logo-mts.png" alt="MTS" width="120" height="48" decoding="async">
        <span class="brand__text">
          <strong class="lang-ar">الموسى للتقنية</strong>
          <strong class="lang-en">AL-MOUSA MTS</strong>
          <small class="lang-ar">وخدمات الأنظمة الأمنية</small>
          <small class="lang-en">Technology &amp; Security</small>
        </span>
      </a>
      <nav class="nav" id="primary-nav" aria-label="Primary">
          {nav}
      </nav>
      <div class="header-actions">
        <button type="button" class="lang-toggle" id="lang-toggle" aria-label="Language">
          <span class="lang-ar">EN</span><span class="lang-en">عربي</span>
        </button>
        <a class="btn btn--sm btn--red" href="contact.html">
          <span class="lang-ar">تواصل معنا</span><span class="lang-en">Contact Us</span>
        </a>
        <button type="button" class="menu-toggle" id="menu-toggle" aria-expanded="false" aria-controls="primary-nav">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>"""


def chrome_footer() -> str:
    return """  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <img src="assets/brand/logo-mts.png" alt="" width="88" height="40" loading="lazy">
        <div>
          <strong class="lang-ar">شركة الموسى للتقنية وخدمات الأنظمة الأمنية</strong>
          <strong class="lang-en">Al-Mousa for Technology and Security Systems Services Co.</strong>
          <p class="lang-ar">إحدى شركات مجموعة الموسى المحدودة · الرياض</p>
          <p class="lang-en">A Subsidiary of Al-Mousa Group Co. Ltd. · Riyadh</p>
        </div>
      </div>
      <div>
        <h3><span class="lang-ar">روابط</span><span class="lang-en">Links</span></h3>
        <div class="footer-links">
          <a href="about.html"><span class="lang-ar">من نحن</span><span class="lang-en">About</span></a>
          <a href="services.html"><span class="lang-ar">الخدمات</span><span class="lang-en">Services</span></a>
          <a href="projects.html"><span class="lang-ar">المشاريع</span><span class="lang-en">Projects</span></a>
          <a href="partners.html"><span class="lang-ar">الشركاء</span><span class="lang-en">Partners</span></a>
        </div>
      </div>
      <div>
        <h3><span class="lang-ar">تواصل</span><span class="lang-en">Contact</span></h3>
        <div class="footer-links">
          <span class="lang-ar">الرياض — المملكة العربية السعودية</span>
          <span class="lang-en">Riyadh — Kingdom of Saudi Arabia</span>
          <a href="contact.html"><span class="lang-ar">صفحة التواصل</span><span class="lang-en">Contact page</span></a>
        </div>
      </div>
    </div>
    <div class="container footer-bottom">
      <p class="lang-ar">© 2026 شركة الموسى للتقنية وخدمات الأنظمة الأمنية.</p>
      <p class="lang-en">© 2026 Al-Mousa for Technology and Security Systems Services Co.</p>
      <p>Corporate Profile 2026 · MTS</p>
    </div>
  </footer>
  <button type="button" class="to-top" id="to-top" aria-label="Top">
    <svg viewBox="0 0 24 24" fill="none"><path d="M12 19V5M5 12l7-7 7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </button>
  <script src="js/main.js" defer></script>"""


def write_page(filename, title_ar, title_en, desc_ar, desc_en, body):
    html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#1E2762">
  <meta name="description" content="{desc_ar}">
  <meta name="title-ar" content="{title_ar}">
  <meta name="title-en" content="{title_en}">
  <meta name="keywords" content="الموسى للتقنية, MTS, أنظمة أمنية, الرياض, Al-Mousa Technology, security systems Saudi Arabia">
  <link rel="canonical" href="https://al-mousa.sa/{filename}">
  <meta property="og:title" content="{title_ar}">
  <meta property="og:description" content="{desc_ar}">
  <meta property="og:type" content="website">
  <title>{title_ar}</title>
  <link rel="icon" type="image/png" href="assets/brand/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Montserrat:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/main.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Organization","name":"Al-Mousa for Technology and Security Systems Services Co.","alternateName":"شركة الموسى للتقنية وخدمات الأنظمة الأمنية","url":"https://al-mousa.sa/","logo":"assets/brand/logo-mts.png","foundingDate":"2021","address":{{"@type":"PostalAddress","addressLocality":"Riyadh","addressCountry":"SA"}},"parentOrganization":{{"@type":"Organization","name":"Al-Mousa Group Co. Ltd."}}}}
  </script>
</head>
<body>
  <a class="skip-link" href="#main"><span class="lang-ar">تخطي إلى المحتوى</span><span class="lang-en">Skip to content</span></a>
{chrome_header(filename)}
  <main id="main">
{body}
  </main>
{chrome_footer()}
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("✓", filename)


def hero(title_ar, title_en, crumb_ar, crumb_en, image):
    return f"""    <section class="page-hero" style="background-image:url('{image}')">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html"><span class="lang-ar">الرئيسية</span><span class="lang-en">Home</span></a>
          <span>/</span>
          <span class="lang-ar">{crumb_ar}</span><span class="lang-en">{crumb_en}</span>
        </nav>
        <p class="eyebrow"><span class="lang-ar">MTS · الموسى للتقنية</span><span class="lang-en">MTS · Al-Mousa Technology</span></p>
        <h1><span class="lang-ar">{title_ar}</span><span class="lang-en">{title_en}</span></h1>
      </div>
    </section>
"""


# ========== INDEX ==========
home = """
    <section class="home-hero">
      <div class="home-hero__media" style="background-image:url('assets/images/hero-riyadh.jpg')" role="img" aria-label="Riyadh skyline"></div>
      <div class="home-hero__stripes" aria-hidden="true"></div>
      <div class="home-hero__content reveal">
        <p class="home-hero__meta">
          <span class="lang-ar">الرياض · المملكة العربية السعودية · الملف المؤسسي ٢٠٢٦</span>
          <span class="lang-en">Riyadh · Kingdom of Saudi Arabia · Corporate Profile 2026</span>
        </p>
        <h1>
          <span class="lang-ar">شركة الموسى للتقنية<br>وخدمات الأنظمة الأمنية</span>
          <span class="lang-en">AL-MOUSA FOR TECHNOLOGY<br>AND SECURITY SYSTEMS SERVICES CO</span>
        </h1>
        <p class="home-hero__tag">
          <span class="lang-ar">إحدى شركات مجموعة الموسى المحدودة — نصوغ دروع حماية رقمية وفيزيائية مبتكرة لاستدامة الأعمال وتأمين الأصول الوطنية الكبرى.</span>
          <span class="lang-en">A Subsidiary of Al-Mousa Group Co. Ltd. — forging innovative digital and physical protection shields for business sustainability and national assets.</span>
        </p>
        <div class="hero-cta">
          <a class="btn btn--red" href="about.html"><span class="lang-ar">اكتشف قصتنا</span><span class="lang-en">Discover Our Story</span></a>
          <a class="btn btn--ghost" href="services.html"><span class="lang-ar">خدماتنا المتكاملة</span><span class="lang-en">Our Solutions</span></a>
        </div>
        <div class="hero-stats">
          <div><strong>2021</strong><span class="lang-ar">سنة التأسيس</span><span class="lang-en">Founded</span></div>
          <div><strong>2030</strong><span class="lang-ar">رؤية المملكة</span><span class="lang-en">Vision aligned</span></div>
          <div><strong>KSA</strong><span class="lang-ar">تغطية وطنية</span><span class="lang-en">Nationwide</span></div>
          <div><strong>MTS</strong><span class="lang-ar">هوية تقنية أمنية</span><span class="lang-en">Security tech</span></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div class="reveal">
          <p class="eyebrow"><span class="lang-ar">من نحن</span><span class="lang-en">About Us</span></p>
          <h2><span class="lang-ar">ذراع تقني متخصص من قلب الرياض</span><span class="lang-en">A specialized technical arm from Riyadh</span></h2>
          <p class="lang-ar">انطلقت شركة الموسى للتقنية وخدمات الأنظمة الأمنية عام ٢٠٢١ من قلب العاصمة الرياض كذراع تقني متخصص لمجموعة الموسى المحدودة. تحت قيادة المؤسس المهندس عبد الكريم الموسى نقود قطاع الحلول الأمنية المتكاملة والبنية التحتية المتقدمة في السوق السعودي.</p>
          <p class="lang-en">Launched in 2021 from Riyadh as a specialized technical arm of Al-Mousa Group. Under Eng. Abdulkarim Al-Mousa we lead integrated security solutions and advanced infrastructure in the Saudi market.</p>
          <p class="lang-ar">نعتز بمساهمتنا في صياغة ملامح رؤية المملكة ٢٠٣٠ عبر المشاركة في تأمين مشاريع وطنية عملاقة مثل أمالا ومشاريع البحر الأحمر.</p>
          <p class="lang-en">We proudly contribute to Vision 2030 through mega projects such as AMAALA and the Red Sea projects.</p>
          <a class="btn btn--outline" href="about.html"><span class="lang-ar">اقرأ المزيد</span><span class="lang-en">Read more</span></a>
        </div>
        <div class="media-frame angled reveal delay-1">
          <img src="assets/images/stock/smart-building.jpg" alt="" loading="lazy" width="900" height="600">
        </div>
      </div>
    </section>

    <section class="section section--soft">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow"><span class="lang-ar">خدماتنا</span><span class="lang-en">Services</span></p>
          <h2><span class="lang-ar">من الدراسة إلى التشغيل عبر نافذة واحدة</span><span class="lang-en">From study to operation — one window</span></h2>
        </div>
        <div class="feature-grid">
          <article class="feature reveal"><h3><span class="lang-ar">الاستشارات والدراسات</span><span class="lang-en">Consulting &amp; Studies</span></h3><p class="lang-ar">مسح ميداني، تحليل متطلبات، تصميم أنظمة، مخططات تنفيذية وBOQ دقيقة.</p><p class="lang-en">Field surveys, requirements analysis, system design, blueprints and precise BOQs.</p></article>
          <article class="feature reveal delay-1"><h3><span class="lang-ar">التنفيذ والتركيب</span><span class="lang-en">Execution &amp; Installation</span></h3><p class="lang-ar">إدارة ميدانية، تمديدات متقنة، وبنية تحتية متكاملة بأعلى كفاءة.</p><p class="lang-en">Field management, masterful cabling, and integrated infrastructure.</p></article>
          <article class="feature reveal delay-2"><h3><span class="lang-ar">الصيانة والدعم</span><span class="lang-en">Maintenance &amp; Support</span></h3><p class="lang-ar">صيانة دورية، دعم فني مستمر، إدارة أعطال طارئة وتحديثات برمجية.</p><p class="lang-en">Periodic maintenance, continuous support, emergency response and updates.</p></article>
          <article class="feature reveal delay-3"><h3><span class="lang-ar">كوادر فنية متخصصة</span><span class="lang-en">Specialized Cadres</span></h3><p class="lang-ar">مهندسون وفنيون وفرق تنفيذ مدربة للدعم الميداني حسب طبيعة كل مشروع.</p><p class="lang-en">Engineers, technicians and trained teams tailored to each project.</p></article>
        </div>
        <div style="text-align:center;margin-top:2rem" class="reveal">
          <a class="btn btn--red" href="services.html"><span class="lang-ar">استعرض كل الخدمات</span><span class="lang-en">View all services</span></a>
        </div>
      </div>
    </section>

    <section class="section section--navy">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow"><span class="lang-ar">المنظومة التقنية</span><span class="lang-en">Technical Ecosystem</span></p>
          <h2><span class="lang-ar">لا نبيع منتجات مجردة — نوطّن حلولاً ذكية</span><span class="lang-en">We localize smart solutions</span></h2>
        </div>
        <div class="card-grid">
          <article class="card reveal">
            <div class="card__img"><img src="assets/images/stock/network-cables.jpg" alt="" loading="lazy" width="700" height="440"></div>
            <div class="card__body"><h3><span class="lang-ar">البنية التحتية والشبكات</span><span class="lang-en">Infrastructure &amp; Networking</span></h3><p class="lang-ar">ألياف ضوئية، كابلات نحاسية، سويتشات، جدار ناري وأنظمة IP.</p><p class="lang-en">Fiber optics, copper cabling, switches, firewalls and IP systems.</p><a class="card__link" href="ecosystem.html"><span class="lang-ar">التفاصيل</span><span class="lang-en">Details</span></a></div>
          </article>
          <article class="card reveal delay-1">
            <div class="card__img"><img src="assets/images/security-shield.jpg" alt="" loading="lazy" width="700" height="440"></div>
            <div class="card__body"><h3><span class="lang-ar">الأمن والحماية</span><span class="lang-en">Security &amp; Protection</span></h3><p class="lang-ar">كاميرات ذكية، تحكم دخول، بصمة، إنذار مبكر وحماية بيانات.</p><p class="lang-en">Smart cameras, access control, biometrics, early warning and data protection.</p><a class="card__link" href="ecosystem.html"><span class="lang-ar">التفاصيل</span><span class="lang-en">Details</span></a></div>
          </article>
          <article class="card reveal delay-2">
            <div class="card__img"><img src="assets/images/stock/datacenter-aisle.jpg" alt="" loading="lazy" width="700" height="440"></div>
            <div class="card__body"><h3><span class="lang-ar">مراكز البيانات والطاقة</span><span class="lang-en">Data Centers &amp; Power</span></h3><p class="lang-ar">غرف بيانات حرجة، تبريد دقيق، UPS، ATS والطاقة الشمسية.</p><p class="lang-en">Critical data rooms, precision cooling, UPS, ATS and solar energy.</p><a class="card__link" href="ecosystem.html"><span class="lang-ar">التفاصيل</span><span class="lang-en">Details</span></a></div>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split split--rev">
        <div class="media-frame reveal"><img src="assets/images/stock/control-room.jpg" alt="" loading="lazy" width="900" height="600"></div>
        <div class="reveal delay-1">
          <p class="eyebrow"><span class="lang-ar">لماذا يختارنا عملاؤنا</span><span class="lang-en">Why Clients Choose Us</span></p>
          <h2><span class="lang-ar">موثوقية عالمية وخبرة ميدانية وطنية</span><span class="lang-en">Global reliability with national expertise</span></h2>
          <div class="quote-band" style="margin:1.5rem 0;clip-path:none">
            <p class="lang-ar">نجمع بين موثوقية الشراكات العالمية والخبرة الميدانية الوطنية لنمنح منشأتك حماية تتوارثها الأجيال.</p>
            <p class="lang-en">We combine global partnership reliability with national field expertise — protection inherited by generations.</p>
          </div>
          <ul class="checklist">
            <li><span class="lang-ar">شراكات واعتمادات عالمية موثوقة</span><span class="lang-en">Trusted global partnerships &amp; accreditations</span></li>
            <li><span class="lang-ar">سجل حافل وإنجازات مثبتة</span><span class="lang-en">Proven track record of success</span></li>
            <li><span class="lang-ar">علاقات مستدامة ودعم مستمر</span><span class="lang-en">Sustained relationships &amp; continuous support</span></li>
            <li><span class="lang-ar">حلول هندسية تغطي دورة حياة المشروع</span><span class="lang-en">End-to-end engineering across the project lifecycle</span></li>
          </ul>
          <a class="btn btn--outline" href="why-us.html" style="margin-top:1rem"><span class="lang-ar">اعرف المزيد</span><span class="lang-en">Learn more</span></a>
        </div>
      </div>
    </section>

    <section class="section section--soft">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow"><span class="lang-ar">أبرز المشاريع</span><span class="lang-en">Key Projects</span></p>
          <h2><span class="lang-ar">حيث تلتقي السرعة بالأمان المطلق</span><span class="lang-en">Where speed meets absolute safety</span></h2>
        </div>
        <div class="project-rail">
          <a class="project-tile reveal" href="projects.html">
            <img src="assets/images/airport-security.jpg" alt="" loading="lazy" width="800" height="500">
            <div class="project-tile__body"><h3><span class="lang-ar">مشاريع المطارات</span><span class="lang-en">Airport Projects</span></h3><p class="lang-ar">الرياض · الدمام · جازان</p><p class="lang-en">Riyadh · Dammam · Jazan</p></div>
          </a>
          <a class="project-tile reveal delay-1" href="projects.html">
            <img src="assets/images/banking.jpg" alt="" loading="lazy" width="800" height="500">
            <div class="project-tile__body"><h3><span class="lang-ar">مشاريع البنوك</span><span class="lang-en">Banking Projects</span></h3><p class="lang-ar">حماية الأصول الرقمية والمعاملات المليارية</p><p class="lang-en">Securing digital assets &amp; multi-billion transactions</p></div>
          </a>
          <a class="project-tile reveal delay-2" href="projects.html">
            <img src="assets/images/government.jpg" alt="" loading="lazy" width="800" height="500">
            <div class="project-tile__body"><h3><span class="lang-ar">المشاريع الحكومية</span><span class="lang-en">Government Projects</span></h3><p class="lang-ar">تأمين البنية التحتية لسيادة الوطن</p><p class="lang-en">Securing the nation's infrastructure</p></div>
          </a>
        </div>
      </div>
    </section>

    <section class="section section--red" style="background-image:url('assets/images/stock/control-room.jpg')">
      <div class="container reveal">
        <div class="section-head">
          <p class="eyebrow"><span class="lang-ar">قيمنا الراسخة</span><span class="lang-en">Our Core Values</span></p>
          <h2><span class="lang-ar">محرك أداء يومي… لا شعارات مكتوبة</span><span class="lang-en">A daily performance engine — not slogans</span></h2>
        </div>
        <div class="pillars">
          <article class="pillar"><h3><span class="lang-ar">الإخلاص في العمل</span><span class="lang-en">Dedication</span></h3><p class="lang-ar">مسؤولية والتزام يفوق تطلعات شركائنا.</p><p class="lang-en">Responsibility exceeding partners' expectations.</p></article>
          <article class="pillar"><h3><span class="lang-ar">الصدق والشفافية</span><span class="lang-en">Honesty</span></h3><p class="lang-ar">وضوح ومصداقية لبناء علاقات مستدامة.</p><p class="lang-en">Clarity and credibility for lasting relationships.</p></article>
          <article class="pillar"><h3><span class="lang-ar">التعاون والتكامل</span><span class="lang-en">Collaboration</span></h3><p class="lang-ar">روح فريق واحد لمخرجات أفضل.</p><p class="lang-en">One team spirit for better outcomes.</p></article>
          <article class="pillar"><h3><span class="lang-ar">الإتقان والتميز</span><span class="lang-en">Excellence</span></h3><p class="lang-ar">تنفيذ دقيق وفق أفضل المعايير.</p><p class="lang-en">Precise execution to the highest standards.</p></article>
        </div>
        <div style="margin-top:2rem"><a class="btn btn--ghost" href="goals.html"><span class="lang-ar">الأهداف والقيم</span><span class="lang-en">Goals &amp; Values</span></a></div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow"><span class="lang-ar">شركاء النجاح</span><span class="lang-en">Success Partners</span></p>
          <h2><span class="lang-ar">شراكات استراتيجية مع نخبة الموردين</span><span class="lang-en">Strategic partnerships with elite suppliers</span></h2>
        </div>
        <div class="logo-wall reveal">
          <figure>Atronika</figure><figure>Atis</figure><figure>Bright Wires</figure>
          <figure>Saudisoft</figure><figure>City Systems</figure><figure>Logicom</figure>
        </div>
        <div style="text-align:center;margin-top:2rem" class="reveal">
          <a class="btn btn--outline" href="partners.html"><span class="lang-ar">الشركاء والعملاء</span><span class="lang-en">Partners &amp; Clients</span></a>
        </div>
      </div>
    </section>

    <section class="section section--soft">
      <div class="container reveal">
        <div class="cta-banner">
          <div>
            <h2><span class="lang-ar">جاهزون لتأمين منشأتك؟</span><span class="lang-en">Ready to secure your facility?</span></h2>
            <p class="lang-ar">تواصل مع فريق الموسى للتقنية لنصمم لك منظومة حماية متكاملة.</p>
            <p class="lang-en">Contact the Al-Mousa Technology team to design an integrated protection ecosystem.</p>
          </div>
          <a class="btn btn--red" href="contact.html"><span class="lang-ar">ابدأ الحوار</span><span class="lang-en">Start a conversation</span></a>
        </div>
      </div>
    </section>
"""

write_page(
    "index.html",
    "الموسى للتقنية وخدمات الأنظمة الأمنية | MTS",
    "Al-Mousa Technology & Security Systems | MTS",
    "شركة الموسى للتقنية وخدمات الأنظمة الأمنية — حلول أمنية وتقنية متكاملة في الرياض.",
    "Al-Mousa for Technology and Security Systems — integrated solutions in Riyadh, KSA.",
    home,
)

# --- inner pages ---
write_page(
    "about.html",
    "من نحن | الموسى للتقنية",
    "About Us | Al-Mousa MTS",
    "تعرف على شركة الموسى للتقنية — ذراع تقني متخصص لمجموعة الموسى من الرياض.",
    "About Al-Mousa Technology — specialized technical arm of Al-Mousa Group.",
    hero("من نحن", "About Us", "من نحن", "About", "assets/images/stock/smart-building.jpg")
    + """
    <section class="section"><div class="container split">
      <div class="prose reveal">
        <p class="eyebrow"><span class="lang-ar">قصتنا</span><span class="lang-en">Our Story</span></p>
        <h2><span class="lang-ar">حيثما وُجدت المنشآت الحيوية وصناعة المستقبل</span><span class="lang-en">Wherever vital facilities and future industries exist</span></h2>
        <p class="lang-ar">يبرز دورنا في صياغة دروع الحماية الرقمية والفيزيائية المبتكرة لتمكين استدامة الأعمال وتأمين الأصول الوطنية الكبرى.</p>
        <p class="lang-en">Our role emerges in forging innovative digital and physical protection shields to enable business sustainability and secure major national assets.</p>
        <p class="lang-ar">انطلقت الشركة عام ٢٠٢١ من قلب الرياض كذراع تقني متخصص متفرع من مجموعة الموسى المحدودة، تحت قيادة المؤسس المهندس عبد الكريم الموسى.</p>
        <p class="lang-en">Launched in 2021 from Riyadh as a specialized technical arm of Al-Mousa Group Co. Ltd., under Eng. Abdulkarim Al-Mousa.</p>
        <p class="lang-ar">نعمل بشغف وكفاءة عالية لتغطية كافة مناطق المملكة، ونعتز بمساهمتنا في رؤية ٢٠٣٠ عبر مشاريع نوعية مثل أمالا والبحر الأحمر.</p>
        <p class="lang-en">We operate nationwide with passion, proudly contributing to Vision 2030 through AMAALA and Red Sea projects.</p>
      </div>
      <div class="reveal delay-1">
        <div class="media-frame" style="margin-bottom:1.2rem"><img src="assets/images/security-shield.jpg" alt="" loading="lazy" width="800" height="500"></div>
        <div class="quote-band" style="clip-path:none"><p class="lang-ar">إن تميزنا لا يقف عند حدود تسليم المشاريع في أوقات قياسية، بل يمتد لبناء علاقات استراتيجية متينة طويلة الأمد ترتكز على الثقة المطلقة.</p><p class="lang-en">Our excellence extends beyond record-time delivery to building solid long-term strategic relationships rooted in absolute trust.</p></div>
      </div>
    </div></section>
    <section class="section section--soft"><div class="container reveal">
      <h2><span class="lang-ar">من نخدم؟</span><span class="lang-en">Who we serve</span></h2>
      <p class="section-lead lang-ar">وزارات وهيئات · حدود ومنافذ · بنوك ومستشفيات · جامعات · مطارات · مشاريع رؤية ٢٠٣٠</p>
      <p class="section-lead lang-en">Ministries · Borders &amp; ports · Banks &amp; hospitals · Universities · Airports · Vision 2030 projects</p>
      <div class="logo-wall" style="margin-top:1.5rem">
        <figure class="lang-ar">وزارات وهيئات</figure><figure class="lang-en">Ministries</figure>
        <figure class="lang-ar">حدود ومنافذ</figure><figure class="lang-en">Borders &amp; Ports</figure>
        <figure class="lang-ar">بنوك ومستشفيات</figure><figure class="lang-en">Banks &amp; Hospitals</figure>
        <figure class="lang-ar">جامعات</figure><figure class="lang-en">Universities</figure>
        <figure class="lang-ar">مطارات</figure><figure class="lang-en">Airports</figure>
        <figure class="lang-ar">رؤية ٢٠٣٠</figure><figure class="lang-en">Vision 2030</figure>
      </div>
    </div></section>
""",
)

write_page(
    "vision.html",
    "الرؤية والرسالة | الموسى للتقنية",
    "Vision & Mission | Al-Mousa MTS",
    "رؤية ورسالة شركة الموسى للتقنية — ريادة وطنية في المشهد الأمني والتقني.",
    "Vision and mission of Al-Mousa Technology.",
    hero("رؤيتنا ورسالتنا", "Vision & Mission", "الرؤية والرسالة", "Vision & Mission", "assets/images/stock/fiber-optics.jpg")
    + """
    <section class="section"><div class="container card-grid">
      <article class="card reveal"><div class="card__body"><p class="eyebrow"><span class="lang-ar">رؤيتنا</span><span class="lang-en">Vision</span></p><h3><span class="lang-ar">ريادة وطنية نصنعها بأيدي كوادرنا</span><span class="lang-en">National leadership by Saudi talents</span></h3><p class="lang-ar">الريادة التزام وطني نصنعه بأيدي كوادرنا السعودية لنكون الواجهة الأولى والشركاء الأوثق في صياغة المشهد الأمني والتقني بالمملكة.</p><p class="lang-en">Leadership is a national commitment forged by Saudi talents — the premier destination and most trusted partner in shaping the Kingdom's security and technology landscape.</p></div></article>
      <article class="card reveal delay-1"><div class="card__body"><p class="eyebrow"><span class="lang-ar">رسالتنا</span><span class="lang-en">Mission</span></p><h3><span class="lang-ar">قيادة الأنظمة الأمنية الذكية</span><span class="lang-en">Leading smart security systems</span></h3><p class="lang-ar">نسعى بثبات نحو قيادة وتوسيع مشاريع الأنظمة الأمنية الذكية، مع تمكين الكوادر الوطنية الشابة للمساهمة في رؤية ٢٠٣٠.</p><p class="lang-en">We lead and expand smart security projects while empowering young national talents to contribute to Vision 2030.</p></div></article>
      <article class="card reveal delay-2"><div class="card__body"><p class="eyebrow"><span class="lang-ar">إيماننا</span><span class="lang-en">Belief</span></p><h3><span class="lang-ar">الحماية هي الخطوة الأولى للنجاح</span><span class="lang-en">Protection is the first step to success</span></h3><p class="lang-ar">حماية مواردك ومنشأتك هي الخطوة الأولى نحو صناعة النجاح، والتزامنا بالجودة والسرعة هو المعادلة الذكية لخفض النفقات وزيادة الإنتاجية.</p><p class="lang-en">Protecting your resources is foundational to success; quality and speed reduce costs and raise productivity.</p></div></article>
    </div></section>
""",
)

write_page(
    "goals.html",
    "الأهداف والقيم | الموسى للتقنية",
    "Goals & Values | Al-Mousa MTS",
    "الأهداف الاستراتيجية والقيم الراسخة لشركة الموسى للتقنية.",
    "Strategic goals and core values of Al-Mousa Technology.",
    hero("أهدافنا وقيمنا", "Goals & Values", "الأهداف والقيم", "Goals & Values", "assets/images/stock/control-room.jpg")
    + """
    <section class="section"><div class="container">
      <div class="section-head reveal"><p class="eyebrow"><span class="lang-ar">أهدافنا الاستراتيجية</span><span class="lang-en">Strategic Goals</span></p>
      <h2><span class="lang-ar">نحرك بوصلة أعمالنا بذكاء</span><span class="lang-en">We intelligently steer our business compass</span></h2>
      <p class="section-lead lang-ar">لتوسيع أثرنا في المشاريع النوعية وترسيخ مكانتنا كشريك أمني عالمي يُدار بأيدي وطنية ماهرة.</p>
      <p class="section-lead lang-en">Expanding impact on qualitative projects as a global security partner managed by skilled national hands.</p></div>
      <div class="feature-grid">
        <article class="feature reveal"><span class="eyebrow">01</span><h3><span class="lang-ar">التوسع الطموح</span><span class="lang-en">Ambitious Expansion</span></h3><p class="lang-ar">تنفيذ المشاريع الكبرى الداعمة لرؤية ٢٠٣٠.</p><p class="lang-en">Executing mega-projects supporting Vision 2030.</p></article>
        <article class="feature reveal delay-1"><span class="eyebrow">02</span><h3><span class="lang-ar">تحالفات استراتيجية</span><span class="lang-en">Strategic Alliances</span></h3><p class="lang-ar">شراكات مع أبرز صناع التقنيات الأمنية العالمية.</p><p class="lang-en">Partnerships with leading global security technology brands.</p></article>
        <article class="feature reveal delay-2"><span class="eyebrow">03</span><h3><span class="lang-ar">تنمية المواهب</span><span class="lang-en">Talent Cultivation</span></h3><p class="lang-ar">استقطاب وتطوير الكوادر الوطنية الماهرة.</p><p class="lang-en">Attracting and developing skilled national cadres.</p></article>
        <article class="feature reveal delay-3"><span class="eyebrow">04</span><h3><span class="lang-ar">معيار موثوق</span><span class="lang-en">Trusted Benchmark</span></h3><p class="lang-ar">ترسيخ مكانتنا كشريك موثوق للأنظمة عالية الجودة.</p><p class="lang-en">Anchoring our position as a trusted high-quality partner.</p></article>
      </div>
    </div></section>
    <section class="section section--soft"><div class="container">
      <div class="section-head reveal"><p class="eyebrow"><span class="lang-ar">قيمنا الراسخة</span><span class="lang-en">Core Values</span></p><h2><span class="lang-ar">محرك الأداء اليومي</span><span class="lang-en">The engine of daily performance</span></h2></div>
      <div class="pillars">
        <article class="pillar reveal"><h3><span class="lang-ar">الإخلاص في العمل</span><span class="lang-en">Dedication</span></h3><p class="lang-ar">أعلى درجات المسؤولية بما يفوق تطلعات شركائنا.</p><p class="lang-en">Highest responsibility exceeding partners' expectations.</p></article>
        <article class="pillar reveal delay-1"><h3><span class="lang-ar">الصدق والشفافية</span><span class="lang-en">Honesty</span></h3><p class="lang-ar">وضوح ومصداقية لبناء علاقات مستدامة.</p><p class="lang-en">Clarity and credibility for lasting relationships.</p></article>
        <article class="pillar reveal delay-2"><h3><span class="lang-ar">التعاون والتكامل</span><span class="lang-en">Collaboration</span></h3><p class="lang-ar">روح الفريق الواحد لنتائج أفضل.</p><p class="lang-en">Unified team spirit for better outcomes.</p></article>
        <article class="pillar reveal delay-3"><h3><span class="lang-ar">الإتقان والتميز</span><span class="lang-en">Excellence</span></h3><p class="lang-ar">تنفيذ دقيق وفق أفضل الممارسات.</p><p class="lang-en">Precise execution to best practices.</p></article>
      </div>
    </div></section>
""",
)

write_page(
    "methodology.html",
    "منهجية العمل | الموسى للتقنية",
    "Work Methodology | Al-Mousa MTS",
    "منهجية العمل والهيكل التنظيمي لشركة الموسى للتقنية.",
    "Work methodology and organizational structure.",
    hero("منهجية العمل", "Work Methodology", "المنهجية", "Methodology", "assets/images/stock/network-cables.jpg")
    + """
    <section class="section"><div class="container split">
      <div class="reveal"><p class="eyebrow"><span class="lang-ar">سر التميز</span><span class="lang-en">Secret of excellence</span></p>
      <h2><span class="lang-ar">تخطيط دقيق وإشراف مكثف</span><span class="lang-en">Meticulous planning &amp; intensive supervision</span></h2>
      <p class="lang-ar">سر تميزنا هما التخطيط الدقيق والإشراف المكثف في تحويل التحديات التقنية إلى واقع تشغيلي آمن وسلس وبزمن قياسي.</p>
      <p class="lang-en">Planning and supervision transform technical challenges into a secure, seamless operational reality in record time.</p></div>
      <div class="table-like reveal delay-1">
        <div class="table-row"><h3><span class="lang-ar">٠١ التخطيط</span><span class="lang-en">01 Planning</span></h3><p class="lang-ar">تحليل المخاطر وتحديد الأهداف ثم حشد الكوادر الفنية المؤهلة.</p><p class="lang-en">Risk analysis, clear goals, then mobilizing qualified cadres.</p></div>
        <div class="table-row"><h3><span class="lang-ar">٠٢ التنفيذ</span><span class="lang-en">02 Execution</span></h3><p class="lang-ar">تنفيذ ميداني سريع مدعوم بإشراف ومتابعة مكثفة وتواصل مستمر.</p><p class="lang-en">Rapid field execution with intensive supervision and communication.</p></div>
        <div class="table-row"><h3><span class="lang-ar">٠٣ ما بعد البيع</span><span class="lang-en">03 After-sales</span></h3><p class="lang-ar">اتصال دائم للاستشارات الفورية والصيانة.</p><p class="lang-en">Permanent communication for consultations and maintenance.</p></div>
      </div>
    </div></section>
    <section class="section section--soft"><div class="container reveal">
      <h2><span class="lang-ar">الهيكل التنظيمي</span><span class="lang-en">Organizational Structure</span></h2>
      <p class="lang-ar">هيكل مرن ومباشر يدمج الكفاءة الإدارية بالخبرة التقنية تحت إدارة المالك المهندس عبد الكريم الموسى، والمدير التنفيذي، والمدير التقني.</p>
      <p class="lang-en">A flexible structure under Owner Eng. Abdulkarim Al-Mousa, the CEO and CTO.</p>
      <div class="logo-wall" style="margin-top:1.5rem">
        <figure><span class="lang-ar">المالك</span><span class="lang-en">Owner</span><br><small>Eng. Abdulkarim Al-Mousa</small></figure>
        <figure>CEO</figure><figure>CTO</figure>
      </div>
    </div></section>
""",
)

write_page(
    "services.html",
    "خدماتنا | الموسى للتقنية",
    "Services | Al-Mousa MTS",
    "خدمات شركة الموسى: استشارات، تنفيذ، صيانة وكوادر فنية.",
    "Al-Mousa services: consulting, execution, maintenance and cadres.",
    hero("خدماتنا المتكاملة", "Our Services", "الخدمات", "Services", "assets/images/stock/control-room.jpg")
    + """
    <section class="section"><div class="container">
      <div class="section-head center reveal"><p class="eyebrow"><span class="lang-ar">مجال الخدمة</span><span class="lang-en">Service Field</span></p>
      <h2><span class="lang-ar">حلول هندسية وتقنية من نافذة واحدة</span><span class="lang-en">Engineering &amp; technical solutions from one window</span></h2></div>
      <div class="table-like">
        <div class="table-row reveal"><h3><span class="lang-ar">الاستشارات والدراسات الهندسية</span><span class="lang-en">Consultations &amp; Engineering Studies</span></h3><p class="lang-ar">مسح ميداني، تحليل متطلبات، تصميم أنظمة مخصصة، مخططات معتمدة وBOQ دقيق.</p><p class="lang-en">Field surveys, requirements analysis, customized design, approved blueprints and precise BOQs.</p></div>
        <div class="table-row reveal delay-1"><h3><span class="lang-ar">التنفيذ والتركيب الاحترافي</span><span class="lang-en">Professional Execution &amp; Installation</span></h3><p class="lang-ar">إدارة وتنفيذ ميداني عبر تمديد وتركيب متقن وبنية تحتية متكاملة.</p><p class="lang-en">Field management through masterful wiring, installation and integrated infrastructure.</p></div>
        <div class="table-row reveal delay-2"><h3><span class="lang-ar">الصيانة وخدمات ما بعد البيع</span><span class="lang-en">Maintenance &amp; After-Sales</span></h3><p class="lang-ar">صيانة دورية، دعم فني مستمر، إدارة أعطال طارئة وتحديثات برمجية.</p><p class="lang-en">Periodic maintenance, continuous support, emergency management and software updates.</p></div>
        <div class="table-row reveal"><h3><span class="lang-ar">توفير الكوادر الفنية المتخصصة</span><span class="lang-en">Specialized Technical Cadres</span></h3><p class="lang-ar">مهندسون وفنيون وفرق تنفيذ مدربة للدعم الميداني حسب كل مشروع.</p><p class="lang-en">Specialized engineers, technicians and trained teams for on-site support.</p></div>
      </div>
    </div></section>
    <section class="section section--soft"><div class="container split">
      <div class="media-frame reveal"><img src="assets/images/stock/cctv.jpg" alt="" loading="lazy" width="800" height="520"></div>
      <div class="reveal delay-1"><h2><span class="lang-ar">راحة بال كاملة لعملائنا</span><span class="lang-en">Total peace of mind</span></h2>
      <p class="lang-ar">من الدراسة والاستشارة وحتى التوريد والتشغيل نوفر منظومة متكاملة تضمن لك راحة البال.</p>
      <p class="lang-en">From study and consultation to supply and operation — an integrated ecosystem.</p>
      <a class="btn btn--red" href="contact.html"><span class="lang-ar">اطلب استشارة</span><span class="lang-en">Request a consultation</span></a></div>
    </div></section>
""",
)

write_page(
    "ecosystem.html",
    "المنظومة التقنية | الموسى للتقنية",
    "Technical Ecosystem | Al-Mousa MTS",
    "المنظومة التقنية ومنتجات الموسى: شبكات، أمن، مراكز بيانات، طاقة وأتمتة.",
    "Al-Mousa technical ecosystem: networking, security, data centers, power and automation.",
    hero("المنظومة التقنية والمنتجات", "Technical Ecosystem", "المنظومة", "Ecosystem", "assets/images/stock/datacenter-aisle.jpg")
    + """
    <section class="section"><div class="container">
      <div class="section-head reveal"><p class="eyebrow"><span class="lang-ar">منتجاتنا</span><span class="lang-en">Products</span></p>
      <h2><span class="lang-ar">حلول ذكية وبنى تحتية فائقة الاعتمادية</span><span class="lang-en">Smart solutions &amp; ultra-reliable infrastructure</span></h2>
      <p class="section-lead lang-ar">موزع معتمد لـ Atronika في المملكة وموزع معتمد لـ Atis العالمية.</p>
      <p class="section-lead lang-en">Authorized distributor for Atronika in KSA and certified distributor for Atis.</p></div>
      <div class="card-grid">
        <article class="card reveal"><div class="card__img"><img src="assets/images/infra.jpg" alt="" loading="lazy"></div><div class="card__body"><h3><span class="lang-ar">البنية التحتية والشبكات</span><span class="lang-en">Infrastructure &amp; Networking</span></h3><p class="lang-ar">ألياف ضوئية، CAT6/6A/7، سويتشات، راوترات، Firewall، IP Telephony وIPTV.</p><p class="lang-en">Fiber, CAT6/6A/7, switches, routers, firewalls, IP telephony &amp; IPTV.</p></div></article>
        <article class="card reveal delay-1"><div class="card__img"><img src="assets/images/stock/cctv-close.jpg" alt="" loading="lazy"></div><div class="card__body"><h3><span class="lang-ar">أنظمة الأمن والحماية</span><span class="lang-en">Security &amp; Protection</span></h3><p class="lang-ar">كاميرات IP &amp; Analog، تسجيل، تحكم دخول، بصمة، إنذار ومكافحة حريق.</p><p class="lang-en">IP &amp; Analog cameras, recording, access control, biometrics, fire systems.</p></div></article>
        <article class="card reveal delay-2"><div class="card__img"><img src="assets/images/datacenter.jpg" alt="" loading="lazy"></div><div class="card__body"><h3><span class="lang-ar">تجهيز مراكز البيانات</span><span class="lang-en">Data Center Preparation</span></h3><p class="lang-ar">كبائن، أرضيات مرتفعة، تبريد دقيق، مراقبة بيئية وتكامل طاقة.</p><p class="lang-en">Cabinets, raised floors, precision cooling, environmental monitoring.</p></div></article>
        <article class="card reveal"><div class="card__img"><img src="assets/images/img-20.jpg" alt="" loading="lazy"></div><div class="card__body"><h3><span class="lang-ar">الكهرباء والطاقة</span><span class="lang-en">Electrical &amp; Power</span></h3><p class="lang-ar">لوحات ذكية، مولدات، ATS، UPS، كفاءة طاقة وأنظمة شمسية.</p><p class="lang-en">Smart boards, generators, ATS, UPS, energy efficiency and solar.</p></div></article>
        <article class="card reveal delay-1"><div class="card__img"><img src="assets/images/stock/smart-building.jpg" alt="" loading="lazy"></div><div class="card__body"><h3><span class="lang-ar">الذكية والأتمتة</span><span class="lang-en">Smart &amp; Automation</span></h3><p class="lang-ar">منازل ومبانٍ ذكية، تحكم إضاءة وتكييف وستائر عبر منصات وتطبيقات.</p><p class="lang-en">Smart homes/buildings, lighting, HVAC and blinds via platforms and apps.</p></div></article>
        <article class="card reveal delay-2"><div class="card__img"><img src="assets/images/img-21.jpg" alt="" loading="lazy"></div><div class="card__body"><h3><span class="lang-ar">الصوتيات والمرئيات</span><span class="lang-en">Audio &amp; Visual</span></h3><p class="lang-ar">نداء عام وصوتيات احترافية وبث محتوى مرئي بإدارة مركزية.</p><p class="lang-en">Professional PA/sound systems and centrally managed visual content.</p></div></article>
      </div>
    </div></section>
""",
)

write_page(
    "why-us.html",
    "لماذا نحن | الموسى للتقنية",
    "Why Choose Us | Al-Mousa MTS",
    "لماذا يختار العملاء شركة الموسى للتقنية شريكاً موثوقاً.",
    "Why clients choose Al-Mousa Technology as a trusted partner.",
    hero("لماذا يختارنا عملاؤنا", "Why Choose Us", "لماذا نحن", "Why Us", "assets/images/stock/handshake.jpg")
    + """
    <section class="section"><div class="container">
      <div class="section-head center reveal"><h2><span class="lang-ar">حماية تتوارثها الأجيال</span><span class="lang-en">Protection inherited by generations</span></h2>
      <p class="section-lead lang-ar">نجمع بين موثوقية الشراكات العالمية والخبرة الميدانية الوطنية.</p>
      <p class="section-lead lang-en">We combine the reliability of global partnerships with skilled national field expertise.</p></div>
      <div class="feature-grid">
        <article class="feature reveal"><h3><span class="lang-ar">شراكات عالمية موثوقة</span><span class="lang-en">Global Partnerships</span></h3><p class="lang-ar">التزام صارم بالمعايير الفنية والتنظيمية في السوق السعودي.</p><p class="lang-en">Strict adherence to technical and regulatory standards in the Saudi market.</p></article>
        <article class="feature reveal delay-1"><h3><span class="lang-ar">سجل إنجازات مثبت</span><span class="lang-en">Proven Track Record</span></h3><p class="lang-ar">خبرة واسعة في المشاريع النوعية المعقدة وبجودة قياسية.</p><p class="lang-en">Deep experience delivering complex qualitative projects at record quality.</p></article>
        <article class="feature reveal delay-2"><h3><span class="lang-ar">دعم مستدام</span><span class="lang-en">Sustained Support</span></h3><p class="lang-ar">لا تنتهي مهمتنا بالتسليم — نرافقك بدعم فني وصيانة ممتدة.</p><p class="lang-en">Our mission continues after delivery with extended support and maintenance.</p></article>
        <article class="feature reveal delay-3"><h3><span class="lang-ar">مرونة وتواصل سلس</span><span class="lang-en">Flexible Communication</span></h3><p class="lang-ar">تجربة تعامل واضحة واستجابة فورية في كل المراحل.</p><p class="lang-en">Transparent dealings and immediate response at every stage.</p></article>
      </div>
      <div class="quote-band reveal" style="margin-top:2rem;clip-path:none"><p class="lang-ar">نغطي دورة حياة المشروع كاملة من المسح والدراسة والتصميم مروراً بالتوريد والتركيب وصولاً للتشغيل الفعلي.</p><p class="lang-en">We cover the full project lifecycle — from survey and design through supply, installation and commissioning.</p></div>
    </div></section>
""",
)

write_page(
    "partners.html",
    "الشركاء والعملاء | الموسى للتقنية",
    "Partners & Clients | Al-Mousa MTS",
    "شركاء النجاح وأبرز عملاء شركة الموسى للتقنية.",
    "Success partners and prominent clients of Al-Mousa Technology.",
    hero("شركاء النجاح والعملاء", "Partners & Clients", "الشركاء", "Partners", "assets/images/stock/handshake.jpg")
    + """
    <section class="section"><div class="container split">
      <div class="reveal"><p class="eyebrow"><span class="lang-ar">شركاء النجاح</span><span class="lang-en">Success Partners</span></p>
      <h2><span class="lang-ar">نخبة الموردين المعتمدين</span><span class="lang-en">An elite of approved suppliers</span></h2>
      <p class="lang-ar">نفخر بشراكاتنا الاستراتيجية مع موردين معتمدين مثل Atronika وAtis بما يعزز قدراتنا التنفيذية وفق أعلى معايير الجودة.</p>
      <p class="lang-en">We pride ourselves on strategic partnerships with approved manufacturers such as Atronika and Atis.</p></div>
      <div class="logo-wall reveal delay-1">
        <figure>Atronika</figure><figure>Atis</figure><figure>Bright Wires</figure>
        <figure>Saudisoft</figure><figure>City Systems</figure><figure>H-Dimension</figure>
        <figure>Vanguard</figure><figure>Logicom</figure><figure>Al-Mousa Group</figure>
      </div>
    </div></section>
    <section class="section section--soft"><div class="container reveal">
      <p class="eyebrow"><span class="lang-ar">أبرز عملائنا</span><span class="lang-en">Prominent Clients</span></p>
      <h2><span class="lang-ar">ثقة عبر قطاعات متعددة</span><span class="lang-en">Trusted across diverse sectors</span></h2>
      <div class="logo-wall" style="margin-top:1.5rem">
        <figure><span class="lang-ar">بنك الرياض</span><span class="lang-en">Riyadh Bank</span></figure>
        <figure><span class="lang-ar">وزارة الإعلام</span><span class="lang-en">Ministry of Media</span></figure>
        <figure><span class="lang-ar">مطار الرياض</span><span class="lang-en">Riyadh Airport</span></figure>
        <figure><span class="lang-ar">مطار الدمام</span><span class="lang-en">Dammam Airport</span></figure>
        <figure><span class="lang-ar">مطار جازان</span><span class="lang-en">Jazan Airport</span></figure>
        <figure><span class="lang-ar">رؤية ٢٠٣٠</span><span class="lang-en">Vision 2030 Projects</span></figure>
      </div>
    </div></section>
""",
)

write_page(
    "projects.html",
    "المشاريع | الموسى للتقنية",
    "Projects | Al-Mousa MTS",
    "أبرز مشاريع الموسى: المطارات والبنوك والجهات الحكومية.",
    "Key Al-Mousa projects: airports, banking and government.",
    hero("أبرز المشاريع", "Key Projects", "المشاريع", "Projects", "assets/images/airport-plane.jpg")
    + """
    <section class="section"><div class="container">
      <article class="split reveal" style="margin-bottom:3rem">
        <div class="media-frame"><img src="assets/images/airport-security.jpg" alt="" loading="lazy"></div>
        <div><p class="eyebrow"><span class="lang-ar">مشاريع المطارات</span><span class="lang-en">Airport Projects</span></p>
        <h2><span class="lang-ar">حيث تلتقي السرعة الفائقة بالأمان المطلق</span><span class="lang-en">Where rapid speed meets absolute safety</span></h2>
        <p class="lang-ar">في بيئة المطارات المتسارعة لا مجال للخطأ. نبتكر بنية رقمية متكاملة وأنظمة أمنية ذكية — كما في مطارات الرياض والدمام وجازان.</p>
        <p class="lang-en">Zero room for error in airports. Digital infrastructure and smart security — delivered at Riyadh, Dammam and Jazan Airports.</p></div>
      </article>
      <article class="split split--rev reveal" style="margin-bottom:3rem">
        <div class="media-frame"><img src="assets/images/banking.jpg" alt="" loading="lazy"></div>
        <div><p class="eyebrow"><span class="lang-ar">مشاريع البنوك</span><span class="lang-en">Banking Projects</span></p>
        <h2><span class="lang-ar">حماية الأصول الرقمية والمعاملات المليارية</span><span class="lang-en">Securing digital assets &amp; multi-billion transactions</span></h2>
        <p class="lang-ar">شبكات فائقة السرعة وحلول أمنية متقدمة — ونفخر بشراكتنا مع مؤسسات مالية كبرى أبرزها بنك الرياض.</p>
        <p class="lang-en">Ultra-high-speed networks and advanced security — notably as a technical partner to Riyadh Bank.</p></div>
      </article>
      <article class="split reveal">
        <div class="media-frame"><img src="assets/images/government.jpg" alt="" loading="lazy"></div>
        <div><p class="eyebrow"><span class="lang-ar">المشاريع الحكومية</span><span class="lang-en">Government Projects</span></p>
        <h2><span class="lang-ar">تأمين البنية التحتية لسيادة الوطن</span><span class="lang-en">Securing the nation's infrastructure</span></h2>
        <p class="lang-ar">شبكات فائقة الكفاءة وحلول أمنية استباقية — ونُعد الخيار المعتمد لجهات رسمية أبرزها وزارة الإعلام.</p>
        <p class="lang-en">Efficient networks and proactive security — trusted by official entities including the Ministry of Media.</p>
        <div class="quote-band" style="margin-top:1.2rem;clip-path:none"><p class="lang-ar">«بين الرؤية والتنفيذ، نصنع قصص نجاح تترجم الطموح إلى واقع.»</p><p class="lang-en">“Between vision and execution, we craft success stories that translate ambition into reality.”</p></div></div>
      </article>
    </div></section>
""",
)

write_page(
    "contact.html",
    "تواصل معنا | الموسى للتقنية",
    "Contact | Al-Mousa MTS",
    "معلومات التواصل مع شركة الموسى للتقنية في الرياض.",
    "Contact information for Al-Mousa Technology in Riyadh.",
    hero("معلومات التواصل", "Contact Information", "تواصل", "Contact", "assets/images/stock/night-city.jpg")
    + """
    <section class="section"><div class="container contact-grid">
      <div class="reveal">
        <p class="eyebrow"><span class="lang-ar">تواصل معنا</span><span class="lang-en">Get in touch</span></p>
        <h2><span class="lang-ar">الرياض — المملكة العربية السعودية</span><span class="lang-en">Riyadh — Kingdom of Saudi Arabia</span></h2>
        <p class="lang-ar">شركة الموسى للتقنية وخدمات الأنظمة الأمنية (إحدى شركات مجموعة الموسى المحدودة)</p>
        <p class="lang-en">Al-Mousa for Technology and Security Systems Services Co. — A Subsidiary of Al-Mousa Group Co. Ltd.</p>
        <div class="media-frame" style="margin-top:1.5rem"><img src="assets/images/stock/smart-building.jpg" alt="" loading="lazy" width="900" height="520"></div>
      </div>
      <dl class="contact-card reveal delay-1">
        <div><dt><span class="lang-ar">المنشأة</span><span class="lang-en">Entity</span></dt>
        <dd><span class="lang-ar">شركة الموسى للتقنية وخدمات الأنظمة الأمنية</span><span class="lang-en">Al-Mousa for Technology and Security Systems Services Co.</span></dd></div>
        <div><dt><span class="lang-ar">المجموعة</span><span class="lang-en">Group</span></dt>
        <dd><span class="lang-ar">مجموعة الموسى المحدودة</span><span class="lang-en">Al-Mousa Group Co. Ltd.</span></dd></div>
        <div><dt><span class="lang-ar">الموقع</span><span class="lang-en">Location</span></dt>
        <dd><span class="lang-ar">الرياض — المملكة العربية السعودية</span><span class="lang-en">Riyadh — Kingdom of Saudi Arabia</span></dd></div>
        <div><dt><span class="lang-ar">التأسيس</span><span class="lang-en">Founded</span></dt><dd>2021</dd></div>
        <div><dt><span class="lang-ar">الإصدار</span><span class="lang-en">Profile Year</span></dt><dd>2026</dd></div>
        <div><dt>Brand</dt><dd>MTS</dd></div>
      </dl>
    </div></section>
""",
)

(ROOT / "README.md").write_text(
    """# Al-Mousa (MTS) Corporate Website

Multi-page bilingual (AR/EN) corporate website for **Al-Mousa for Technology and Security Systems Services Co.**

Visual identity follows the 2026 corporate profile: navy `#1E2762`, red `#BC1F28`, diagonal motifs, MTS branding, and imagery from the company profile plus professional stock photography.

## Pages
- `index.html` — long visual homepage
- `about.html` · `vision.html` · `goals.html` · `methodology.html`
- `services.html` · `ecosystem.html` · `why-us.html`
- `partners.html` · `projects.html` · `contact.html`

## Run
```bash
python3 -m http.server 8080
```
""",
    encoding="utf-8",
)
print("DONE")
