---
layout: default
title: 学术成果
---

{% assign featured_paper = site.data.publications | first %}
{% include page-header.html header=site.publications_header accent="blue" %}

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-14 md:py-20">
  <div class="stage-shell px-6 py-8 md:px-10 md:py-10" data-stage="featured-publication" data-reveal="scale">
    <div class="grid gap-8 xl:grid-cols-[1.08fr_0.92fr] xl:items-end">
      <div>
        <p class="section-kicker text-[0.72rem] font-black uppercase text-sky-600 dark:text-cyan-300">
          <span class="lang-zh">精选成果主舞台</span>
          <span class="lang-en">Featured Main Stage</span>
        </p>

        <h2 class="mt-4 text-3xl font-black leading-tight text-slate-900 dark:text-white md:text-5xl">
          <span class="lang-zh">先让代表性工作被看见，再进入完整年份章节</span>
          <span class="lang-en">See the Signature Work First, Then Enter the Yearly Archive</span>
        </h2>

        <p class="mt-5 max-w-3xl text-base leading-relaxed text-slate-600 dark:text-slate-300 md:text-lg">
          <span class="lang-zh">这一页不把所有论文都压成同一种密度。我们让代表性成果先站到前面，再把剩余论文放进按年份组织的纵向轨道里。</span>
          <span class="lang-en">This page does not compress every paper into the same density. Signature work leads the story, and the remaining papers are organized into a year-driven vertical track.</span>
        </p>
      </div>

      <div class="panel-surface p-5 md:p-6">
        <p class="section-kicker text-[0.68rem] font-black uppercase text-slate-400 dark:text-slate-500">
          <span class="lang-zh">当前锚点</span>
          <span class="lang-en">Current Anchor</span>
        </p>
        <p class="mt-3 text-sm font-bold uppercase tracking-[0.18em] text-slate-400 dark:text-slate-500">{{ featured_paper.year }} · {{ featured_paper.venue.en | default: featured_paper.venue }}</p>
        <p class="mt-3 text-xl font-black leading-snug text-slate-900 dark:text-white">
          <span class="lang-zh">{{ featured_paper.title.zh | default: featured_paper.title }}</span>
          <span class="lang-en">{{ featured_paper.title.en | default: featured_paper.title }}</span>
        </p>
        <p class="mt-4 text-sm leading-relaxed text-slate-500 dark:text-slate-400">{{ featured_paper.authors }}</p>
      </div>
    </div>

    <div class="mt-8 grid gap-6 xl:grid-cols-[1.06fr_0.94fr] xl:items-end">
      {% include publication-card.html
        paper=featured_paper
        variant="feature"
        outer_class="p-6 md:p-8"
        inner_class="lg:grid-cols-[0.94fr_1.06fr] lg:items-end"
        image_class="h-72 w-full object-cover md:h-80"
        show_abstract=true
        show_actions=true
      %}

      <div class="grid gap-5">
        {% for paper in site.data.publications offset:1 limit:3 %}
        {% assign publication_preview_href = paper.links.paper | default: "/pages/publications.html" %}
        {% include publication-card.html
          paper=paper
          variant="summary"
          href=publication_preview_href
          outer_class="p-5"
          meta_secondary="year"
        %}
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pb-8">
  {% assign grouped_papers = site.data.publications | group_by: "year" | sort: "name" | reverse %}

  <div class="space-y-14">
    {% for year_group in grouped_papers %}
    <div class="grid gap-6 xl:grid-cols-[10rem_1fr]">
      <div class="year-rail" data-reveal="left">
        <div class="year-rail__value">{{ year_group.name }}</div>
      </div>

      <div class="space-y-5">
        {% for paper in year_group.items %}
        {% unless paper.title.en == featured_paper.title.en %}
          {% if paper.image and forloop.first %}
          {% include publication-card.html
            paper=paper
            variant="feature"
            outer_class="p-6 md:p-7"
            inner_class="lg:grid-cols-[0.86fr_1.14fr] lg:items-end"
            image_class="h-64 w-full object-cover md:h-72"
            reveal="scale"
            show_abstract=true
            show_actions=true
          %}
          {% else %}
          {% include publication-card.html
            paper=paper
            variant="summary"
            outer_class="p-5 md:p-6"
            reveal="right"
            meta_secondary="venue"
            show_abstract=true
            show_actions=true
            show_highlight=true
          %}
          {% endif %}
        {% endunless %}
        {% endfor %}
      </div>
    </div>
    {% endfor %}
  </div>
</section>

{% include narrative-band.html band=site.cta_bands.publications accent="sky" %}
