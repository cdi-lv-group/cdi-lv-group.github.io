---
layout: default
title: 首页
---

{% assign research_count = site.data.research | size %}
{% assign publication_count = site.data.publications | size %}
{% assign news_count = site.data.news | size %}
{% assign position_count = site.data.positions | size %}
{% assign latest_news = site.data.news | first %}
{% assign latest_paper = site.data.publications | first %}

<section class="relative overflow-hidden pt-10 pb-16 md:pb-24">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid gap-10 xl:grid-cols-[1.02fr_0.98fr] xl:items-end">
      <div data-reveal="left">
        <div class="inline-flex items-center gap-3 rounded-full border border-white/80 bg-white/70 px-5 py-2 text-sm font-semibold tracking-wide text-sky-700 shadow-sm backdrop-blur dark:border-slate-700/80 dark:bg-slate-900/70 dark:text-cyan-300">
          <span class="relative flex h-2.5 w-2.5">
            <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-cyan-400 opacity-75"></span>
            <span class="relative inline-flex h-2.5 w-2.5 rounded-full bg-sky-500"></span>
          </span>
          <span class="lang-zh">{{ site.hero.badge.zh }}</span>
          <span class="lang-en">{{ site.hero.badge.en }}</span>
        </div>

        {% if site.hero.eyebrow_notes %}
        <div class="mt-5 flex flex-wrap gap-2">
          {% for note in site.hero.eyebrow_notes %}
          <span class="chip text-[11px] font-black uppercase tracking-[0.16em] text-slate-500 dark:text-slate-300">
            <span class="lang-zh">{{ note.zh }}</span>
            <span class="lang-en">{{ note.en }}</span>
          </span>
          {% endfor %}
        </div>
        {% endif %}

        <h1 class="mt-7 text-5xl font-black leading-[0.96] text-slate-900 dark:text-white md:text-7xl">
          <span class="lang-zh">
            {{ site.hero.title_main.zh }}
            <span class="block text-transparent bg-clip-text bg-gradient-to-r from-sky-600 via-cyan-500 to-teal-500 dark:from-sky-300 dark:via-cyan-300 dark:to-teal-300">{{ site.hero.title_gradient.zh }}</span>
          </span>
          <span class="lang-en">
            {{ site.hero.title_main.en }}
            <span class="block text-transparent bg-clip-text bg-gradient-to-r from-sky-600 via-cyan-500 to-teal-500 dark:from-sky-300 dark:via-cyan-300 dark:to-teal-300">{{ site.hero.title_gradient.en }}</span>
          </span>
        </h1>

        <p class="mt-8 max-w-3xl text-lg leading-relaxed text-slate-600 dark:text-slate-300 md:text-xl">
          <span class="lang-zh">{{ site.hero.description.zh }}</span>
          <span class="lang-en">{{ site.hero.description.en }}</span>
        </p>

        <div class="mt-10 flex flex-col gap-4 sm:flex-row">
          <a href="{{ site.hero.primary_btn.url | relative_url }}" class="inline-flex items-center justify-center rounded-2xl bg-slate-900 px-7 py-4 text-base font-black text-white transition-all duration-300 hover:-translate-y-1 hover:bg-sky-600 hover:shadow-2xl dark:bg-white dark:text-slate-900 dark:hover:bg-cyan-300">
            <span class="lang-zh">{{ site.hero.primary_btn.text.zh }}</span>
            <span class="lang-en">{{ site.hero.primary_btn.text.en }}</span>
          </a>
          <a href="{{ site.hero.secondary_btn.url | relative_url }}" class="inline-flex items-center justify-center rounded-2xl border border-slate-200/80 bg-white/70 px-7 py-4 text-base font-bold text-slate-700 transition-all duration-300 hover:-translate-y-1 hover:border-sky-200 hover:text-sky-600 dark:border-slate-700/80 dark:bg-slate-900/70 dark:text-slate-200 dark:hover:border-cyan-400 dark:hover:text-cyan-300">
            <span class="lang-zh">{{ site.hero.secondary_btn.text.zh }}</span>
            <span class="lang-en">{{ site.hero.secondary_btn.text.en }}</span>
          </a>
        </div>

        <div class="mt-10 grid gap-4 md:grid-cols-6">
          <div class="stage-rail p-5 md:col-span-2">
            <p class="section-kicker text-[0.68rem] font-black uppercase text-sky-600 dark:text-cyan-300">
              <span class="lang-zh">研究展示系统</span>
              <span class="lang-en">Research Display System</span>
            </p>
            <p class="mt-3 text-lg font-black leading-snug text-slate-900 dark:text-white">
              <span class="lang-zh">以研究方向、成果陈列与实验室时间线构成完整浏览路径。</span>
              <span class="lang-en">A complete browsing path built from research themes, publication staging, and a lab timeline.</span>
            </p>
          </div>

          <div class="panel-surface p-4 md:col-span-1">
            <p class="section-kicker text-[0.62rem] font-black uppercase text-slate-400 dark:text-slate-500">
              <span class="lang-zh">方向</span>
              <span class="lang-en">Areas</span>
            </p>
            <p class="mt-2 text-3xl font-black text-slate-900 dark:text-white">{{ research_count }}</p>
          </div>

          <div class="panel-surface p-4 md:col-span-1">
            <p class="section-kicker text-[0.62rem] font-black uppercase text-slate-400 dark:text-slate-500">
              <span class="lang-zh">论文</span>
              <span class="lang-en">Papers</span>
            </p>
            <p class="mt-2 text-3xl font-black text-slate-900 dark:text-white">{{ publication_count }}</p>
          </div>

          <div class="panel-surface p-4 md:col-span-1">
            <p class="section-kicker text-[0.62rem] font-black uppercase text-slate-400 dark:text-slate-500">
              <span class="lang-zh">新闻</span>
              <span class="lang-en">Updates</span>
            </p>
            <p class="mt-2 text-3xl font-black text-slate-900 dark:text-white">{{ news_count }}</p>
          </div>

          <div class="panel-surface p-4 md:col-span-1">
            <p class="section-kicker text-[0.62rem] font-black uppercase text-slate-400 dark:text-slate-500">
              <span class="lang-zh">岗位</span>
              <span class="lang-en">Openings</span>
            </p>
            <p class="mt-2 text-3xl font-black text-slate-900 dark:text-white">{{ position_count }}</p>
          </div>
        </div>
      </div>

      <div data-reveal="scale">
        <div class="stage-shell p-4 md:p-6" data-stage="home-hero">
          <div class="relative overflow-hidden rounded-[2rem] border border-white/70 dark:border-slate-700/80">
            <div class="absolute right-6 top-5 z-20 text-[5rem] font-black tracking-[-0.12em] text-white/20">01</div>
            <div class="absolute inset-0 z-10 bg-gradient-to-t from-slate-950/68 via-slate-900/18 to-sky-500/10"></div>
            <img src="{{ site.hero.image }}" alt="Hero Visual" class="h-[420px] w-full object-cover md:h-[560px]">

            {% if latest_news %}
            <div class="panel-surface absolute left-5 top-5 z-20 max-w-xs p-4">
              <p class="section-kicker text-[0.64rem] font-black uppercase text-sky-600 dark:text-cyan-300">
                <span class="lang-zh">最新动态</span>
                <span class="lang-en">Latest Update</span>
              </p>
              <p class="mt-2 text-xs font-bold uppercase tracking-[0.18em] text-slate-400 dark:text-slate-500">{{ latest_news.date }}</p>
              <p class="mt-3 text-sm font-bold leading-snug text-slate-900 dark:text-white">
                <span class="lang-zh">{{ latest_news.title.zh | default: latest_news.title }}</span>
                <span class="lang-en">{{ latest_news.title.en | default: latest_news.title }}</span>
              </p>
            </div>
            {% endif %}

            {% if latest_paper %}
            <div class="stage-rail absolute bottom-5 right-5 z-20 max-w-sm p-5">
              <p class="section-kicker text-[0.64rem] font-black uppercase text-sky-600 dark:text-cyan-300">
                <span class="lang-zh">精选成果</span>
                <span class="lang-en">Featured Work</span>
              </p>
              <p class="mt-3 text-xs font-black uppercase tracking-[0.18em] text-slate-400 dark:text-slate-500">{{ latest_paper.venue.en | default: latest_paper.venue }}</p>
              <p class="mt-2 text-base font-bold leading-snug text-slate-900 dark:text-white">
                <span class="lang-zh">{{ latest_paper.title.zh | default: latest_paper.title }}</span>
                <span class="lang-en">{{ latest_paper.title.en | default: latest_paper.title }}</span>
              </p>
            </div>
            {% endif %}

            {% if site.hero.stage_tags %}
            <div class="absolute bottom-5 left-5 z-20 flex max-w-md flex-wrap gap-2">
              {% for tag in site.hero.stage_tags %}
              <span class="chip border-white/20 bg-slate-950/45 text-[11px] font-black uppercase tracking-[0.14em] text-white">
                <span class="lang-zh">{{ tag.zh }}</span>
                <span class="lang-en">{{ tag.en }}</span>
              </span>
              {% endfor %}
            </div>
            {% endif %}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-20">
  <div class="grid gap-10 xl:grid-cols-[0.62fr_1.38fr] xl:items-start">
    {% include chapter-intro.html
      serial="01"
      accent="sky"
      reveal="left"
      kicker_zh="研究版图"
      kicker_en="Research Landscape"
      title_zh="用更像展陈目录的方式浏览研究方向"
      title_en="Browse Our Themes Like a Curated Exhibition Atlas"
      description_zh="从空间地图、世界模型到设计智能与文档系统，我们把研究链路拆成可以被快速理解、跳转和延伸阅读的章节。"
      description_en="From spatial maps and world models to design intelligence and document systems, the research pipeline is organized into chapters that are easy to understand, jump through, and revisit."
      link_url="/pages/research.html"
      link_text_zh="进入研究展陈页"
      link_text_en="Enter Research Gallery"
    %}

    <div class="grid gap-6 xl:grid-cols-[1.08fr_0.92fr]">
      {% for item in site.data.research limit:1 %}
      <a href="{{ '/pages/research.html#area-1' | relative_url }}" class="feature-card p-6 md:p-8 xl:min-h-[33rem]" data-reveal="scale">
        <div class="feature-card__ghost">01</div>
        <div class="relative z-10 flex h-full flex-col">
          <div class="flex items-center gap-4">
            <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-sky-50 text-4xl text-sky-600 dark:bg-slate-800 dark:text-cyan-300">{{ item.icon }}</div>
            <div class="chip text-[11px] font-black uppercase tracking-[0.14em] text-slate-500 dark:text-slate-300">
              <span class="lang-zh">主舞台方向</span>
              <span class="lang-en">Main Stage Theme</span>
            </div>
          </div>

          <h3 class="mt-8 text-3xl font-black leading-tight text-slate-900 dark:text-white">
            <span class="lang-zh">{{ item.title.zh | default: item.title }}</span>
            <span class="lang-en">{{ item.title.en | default: item.title }}</span>
          </h3>

          <p class="mt-5 max-w-2xl text-base leading-relaxed text-slate-600 dark:text-slate-300 md:text-lg">
            <span class="lang-zh">{{ item.description.zh | default: item.description }}</span>
            <span class="lang-en">{{ item.description.en | default: item.description }}</span>
          </p>

          {% if item.image %}
          <div class="research-media mt-8">
            <img src="{{ site.baseurl }}{{ item.image }}" alt="{{ item.title.zh | default: item.title }}" class="h-64 w-full object-cover md:h-72">
          </div>
          {% endif %}
        </div>
      </a>
      {% endfor %}

      <div class="grid gap-6">
        {% for item in site.data.research offset:1 limit:2 %}
        {% assign research_preview_index = forloop.index | plus: 1 %}
        <a href="{{ site.baseurl }}/pages/research.html#area-{{ research_preview_index }}" class="feature-card p-6" data-reveal="right">
          <div class="relative z-10">
            <div class="flex items-center gap-3">
              <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-white/80 text-3xl text-sky-600 shadow-sm dark:bg-slate-900/70 dark:text-cyan-300">{{ item.icon }}</div>
              <span class="text-xs font-black uppercase tracking-[0.18em] text-slate-400 dark:text-slate-500">0{{ research_preview_index }}</span>
            </div>
            <h3 class="mt-5 text-2xl font-black leading-tight text-slate-900 dark:text-white">
              <span class="lang-zh">{{ item.title.zh | default: item.title }}</span>
              <span class="lang-en">{{ item.title.en | default: item.title }}</span>
            </h3>
            <p class="mt-3 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
              <span class="lang-zh">{{ item.description.zh | default: item.description }}</span>
              <span class="lang-en">{{ item.description.en | default: item.description }}</span>
            </p>
          </div>
        </a>
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10 md:py-16">
  <div class="grid gap-10 xl:grid-cols-[1.12fr_0.88fr] xl:items-start">
    <div class="grid gap-5" data-reveal="left">
      {% for item in site.data.news limit:3 %}
      {% include news-card.html
        item=item
        variant="timeline"
        outer_class="p-5 md:p-6"
        fallback_href="/pages/news.html"
        title_is_link=true
        compact_category=true
      %}
      {% endfor %}
    </div>

    {% include chapter-intro.html
      serial="02"
      accent="sky"
      reveal="right"
      extra_class="xl:order-first"
      kicker_zh="实验室时间线"
      kicker_en="Lab Timeline"
      title_zh="论文、合作与系统建设在同一时间轴里展开"
      title_en="Papers, Collaborations, and Systems Unfold on One Timeline"
      description_zh="首页保留一条更紧凑的时间线入口，帮助访问者先快速理解实验室最近在发生什么，再决定进入更完整的新闻页面。"
      description_en="The home page keeps a compact timeline so visitors can quickly understand what the lab has been doing recently before diving into the full news page."
      link_url="/pages/news.html"
      link_text_zh="浏览完整时间线"
      link_text_en="Browse Full Timeline"
    %}
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
  <div class="grid gap-10 xl:grid-cols-[0.6fr_1.4fr] xl:items-start">
    {% include chapter-intro.html
      serial="03"
      accent="sky"
      reveal="left"
      kicker_zh="代表成果"
      kicker_en="Featured Work"
      title_zh="把论文呈现成更像成果陈列而不是普通列表"
      title_en="Present Publications as a Gallery Rather Than a Plain List"
      description_zh="我们让精选论文先占据主舞台，再用紧凑卡片补充其余成果。这样用户能先感受到代表性工作，再进入完整年份章节。"
      description_en="A featured publication takes the main stage first, while compact cards extend the rest of the story. Visitors encounter representative work before opening the full year-based archive."
      link_url="/pages/publications.html"
      link_text_zh="进入成果陈列页"
      link_text_en="Enter Publication Gallery"
    %}

    <div class="grid gap-6 xl:grid-cols-[1.1fr_0.9fr]">
      {% for paper in site.data.publications limit:1 %}
      {% assign home_featured_paper_href = paper.links.paper | default: "/pages/publications.html" %}
      {% include publication-card.html
        paper=paper
        variant="feature"
        href=home_featured_paper_href
        outer_class="p-6 md:p-8"
        inner_class="lg:grid-cols-[0.96fr_1.04fr] lg:items-end"
        image_class="h-72 w-full object-cover"
        reveal="scale"
        ghost="03"
        show_abstract=true
      %}
      {% endfor %}

      <div class="grid gap-5">
        {% for paper in site.data.publications offset:1 limit:2 %}
        {% assign home_paper_href = paper.links.paper | default: "/pages/publications.html" %}
        {% include publication-card.html
          paper=paper
          variant="summary"
          href=home_paper_href
          outer_class="p-5"
          reveal="right"
          meta_secondary="year"
        %}
        {% endfor %}
      </div>
    </div>
  </div>
</section>

{% include narrative-band.html band=site.cta_bands.join accent="sky" %}
