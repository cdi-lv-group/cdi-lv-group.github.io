(() => {
  const root = document.documentElement;
  const themeStorageKey = "color-theme";
  const langStorageKey = "lang";

  const syncLangButtons = () => {
    const currentLang = root.lang || "zh";
    document.querySelectorAll("[data-set-lang]").forEach((button) => {
      button.classList.toggle("is-active", button.dataset.setLang === currentLang);
    });
  };

  const syncThemeIcons = () => {
    const isDark = root.classList.contains("dark");
    document.querySelectorAll('[data-theme-icon="dark"]').forEach((icon) => {
      icon.classList.toggle("hidden", isDark);
    });
    document.querySelectorAll('[data-theme-icon="light"]').forEach((icon) => {
      icon.classList.toggle("hidden", !isDark);
    });
  };

  const syncMenuState = () => {
    const menu = document.querySelector("[data-mobile-menu]");
    const toggle = document.querySelector("[data-toggle-menu]");
    if (!menu || !toggle) {
      return;
    }
    toggle.setAttribute("aria-expanded", String(menu.classList.contains("is-open")));
  };

  const setLang = (lang) => {
    root.lang = lang;
    localStorage.setItem(langStorageKey, lang);

    const url = new URL(window.location.href);
    url.searchParams.set("lang", lang);
    window.history.replaceState({}, "", url);

    syncLangButtons();
  };

  const setTheme = (theme) => {
    root.classList.toggle("dark", theme === "dark");
    localStorage.setItem(themeStorageKey, theme);
    syncThemeIcons();
  };

  const toggleMenu = () => {
    const menu = document.querySelector("[data-mobile-menu]");
    if (!menu) {
      return;
    }
    menu.classList.toggle("is-open");
    syncMenuState();
  };

  const setupReveal = () => {
    const items = Array.from(document.querySelectorAll("[data-reveal]"));
    if (!items.length) {
      return;
    }

    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    root.classList.add("reveal-ready");

    if (reduceMotion.matches || !("IntersectionObserver" in window)) {
      items.forEach((item) => item.classList.add("is-visible"));
      return;
    }

    items.forEach((item, index) => {
      const delay = item.dataset.revealDelay || `${Math.min(index * 55, 260)}ms`;
      item.style.setProperty("--reveal-delay", delay);
    });

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) {
            return;
          }
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      {
        rootMargin: "0px 0px -8% 0px",
        threshold: 0.14,
      }
    );

    items.forEach((item) => observer.observe(item));
  };

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-set-lang]").forEach((button) => {
      button.addEventListener("click", () => {
        setLang(button.dataset.setLang || "zh");
      });
    });

    document.querySelectorAll("[data-toggle-theme]").forEach((button) => {
      button.addEventListener("click", () => {
        setTheme(root.classList.contains("dark") ? "light" : "dark");
      });
    });

    document.querySelectorAll("[data-toggle-menu]").forEach((button) => {
      button.addEventListener("click", toggleMenu);
    });

    document.querySelectorAll("[data-mobile-menu] a").forEach((link) => {
      link.addEventListener("click", () => {
        const menu = document.querySelector("[data-mobile-menu]");
        if (!menu) {
          return;
        }
        menu.classList.remove("is-open");
        syncMenuState();
      });
    });

    const desktopBreakpoint = window.matchMedia("(min-width: 768px)");
    const closeMenuOnDesktop = () => {
      if (!desktopBreakpoint.matches) {
        return;
      }
      const menu = document.querySelector("[data-mobile-menu]");
      if (!menu) {
        return;
      }
      menu.classList.remove("is-open");
      syncMenuState();
    };

    if (desktopBreakpoint.addEventListener) {
      desktopBreakpoint.addEventListener("change", closeMenuOnDesktop);
    } else {
      desktopBreakpoint.addListener(closeMenuOnDesktop);
    }

    syncLangButtons();
    syncThemeIcons();
    syncMenuState();
    setupReveal();
  });

  window.switchLang = setLang;
})();
