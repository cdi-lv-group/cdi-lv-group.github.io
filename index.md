---
layout: default
title: 首页
---

{% comment %} 
  逻辑判断：获取当前语言
{% endcomment %}
{% assign curr_lang = "zh" %}
{% if page.url contains '/en/' %}
  {% assign curr_lang = "en" %}
{% endif %}

<section class="relative py-20 md:py-32 overflow-hidden">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full -z-10">
        <div class="absolute top-[-10%] left-[-10%] w-[40%] h-[60%] bg-blue-50 dark:bg-blue-900/10 rounded-full blur-[120px] opacity-60"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[40%] h-[60%] bg-cyan-50 dark:bg-cyan-900/10 rounded-full blur-[120px] opacity-60"></div>
    </div>

    <div class="max-w-6xl mx-auto px-4">
        <div class="flex flex-col md:flex-row items-center gap-12">
            <div class="flex-1 text-center md:text-left">
                <h1 class="text-4xl md:text-6xl font-extrabold text-slate-900 dark:text-white mb-6 leading-[1.1] tracking-tight">
                    {% if curr_lang == "zh" %}
                        探索 <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500">智能交互</span> <br> 与视觉感知的边界
                    {% else %}
                        Exploring the Boundaries of <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500">Intelligent Interaction</span> & Perception
                    {% endif %}
                </h1>
                <p class="text-lg md:text-xl text-slate-600 dark:text-slate-400 mb-10 leading-relaxed font-light">
                    {% if curr_lang == "zh" %}
                        {{ site.description }} 我们专注于多模态感知、具身智能以及人机交互的前沿研究。
                    {% else %}
                        We focus on cutting-edge research in multi-modal perception, embodied AI, and human-computer interaction.
                    {% endif %}
                </p>
                <div class="flex flex-wrap justify-center md:justify-start gap-4">
                    <a href="{% if curr_lang == 'en' %}/en{% endif %}/pages/research.html" class="px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-2xl font-bold transition-all shadow-lg shadow-blue-200 dark:shadow-none hover:-translate-y-1">
                        {% if curr_lang == "zh" %}研究方向{% else %}Research Areas{% endif %}
                    </a>
                    <a href="{% if curr_lang == 'en' %}/en{% endif %}/pages/contact.html" class="px-8 py-4 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 rounded-2xl font-bold hover:bg-slate-50 dark:hover:bg-slate-700 transition-all">
                        {% if curr_lang == "zh" %}加入我们{% else %}Join Us{% endif %}
                    </a>
                </div>
            </div>
            
            <div class="flex-1 relative w-full max-w-lg">
                <div class="aspect-square bg-gradient-to-br from-blue-100 to-cyan-50 dark:from-slate-800 dark:to-slate-700 rounded-[3rem] rotate-3 relative overflow-hidden shadow-2xl">
                    <div class="absolute inset-0 flex items-center justify-center text-8xl">
                        🤖
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-12 border-y border-slate-100 dark:border-slate-800">
    <div class="max-w-6xl mx-auto px-4">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div>
                <div class="text-3xl font-bold text-slate-900 dark:text-white">20+</div>
                <div class="text-sm text-slate-500">{% if curr_lang == "zh" %}核心成员{% else %}Core Members{% endif %}</div>
            </div>
            <div>
                <div class="text-3xl font-bold text-slate-900 dark:text-white">50+</div>
                <div class="text-sm text-slate-500">{% if curr_lang == "zh" %}学术论文{% else %}Publications{% endif %}</div>
            </div>
            <div>
                <div class="text-3xl font-bold text-slate-900 dark:text-white">10+</div>
                <div class="text-sm text-slate-500">{% if curr_lang == "zh" %}开源项目{% else %}Open Source{% endif %}</div>
            </div>
            <div>
                <div class="text-3xl font-bold text-slate-900 dark:text-white">5+</div>
                <div class="text-sm text-slate-500">{% if curr_lang == "zh" %}产业合作{% else %}Partnerships{% endif %}</div>
            </div>
        </div>
    </div>
</section>

<section class="py-20 bg-slate-50/50 dark:bg-slate-900/50">
    <div class="max-w-6xl mx-auto px-4">
        <div class="flex justify-between items-end mb-12">
            <div>
                <h2 class="text-3xl font-bold text-slate-900 dark:text-white mb-2">{% if curr_lang == "zh" %}最新动态{% else %}Latest News{% endif %}</h2>
                <p class="text-slate-500">{% if curr_lang == "zh" %}了解实验室的近况{% else %}Stay updated with our progress{% endif %}</p>
            </div>
            <a href="{% if curr_lang == 'en' %}/en{% endif %}/pages/news.html" class="text-blue-600 dark:text-blue-400 font-semibold hover:underline">
                {% if curr_lang == "zh" %}查看全部{% else %}View All{% endif %} →
            </a>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
            {% for item in site.data.news limit:3 %}
            <div class="bg-white dark:bg-slate-800 p-6 rounded-3xl border border-slate-100 dark:border-slate-700 shadow-sm">
                <span class="text-xs font-bold text-blue-600 dark:text-blue-400 uppercase tracking-widest">{{ item.date }}</span>
                <h3 class="text-xl font-bold text-slate-900 dark:text-white mt-3 mb-4 leading-snug">
                    {{ item['title_' | append: curr_lang] | default: item.title }}
                </h3>
                <p class="text-slate-500 dark:text-slate-400 text-sm line-clamp-2">
                    {{ item['description_' | append: curr_lang] | default: item.description }}
                </p>
            </div>
            {% endfor %}
        </div>
    </div>
</section>