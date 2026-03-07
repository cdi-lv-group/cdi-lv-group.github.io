---
layout: default
title: 首页
---

<section class="py-20 bg-gradient-to-b from-white to-slate-50">
  <div class="max-w-4xl mx-auto px-4 text-center">
    <h1 class="text-5xl font-extrabold text-slate-900 mb-6">
      专注于 <span class="text-blue-600">3D感知、具身智能</span> 与视觉交互
    </h1>
    <p class="text-xl text-slate-600 mb-10">
      致力于多模态感知、推理与交互的共性基础研究，探索空天智能与智能体交互的前沿边界。
    </p>
    <div class="flex justify-center space-x-4">
      <a href="/people" class="bg-blue-600 text-white px-8 py-3 rounded-full font-semibold hover:bg-blue-700 transition">了解团队</a>
      <a href="/research" class="bg-white border border-slate-200 text-slate-700 px-8 py-3 rounded-full font-semibold hover:shadow-sm transition">研究方向</a>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16">
  <div class="grid md:grid-cols-3 gap-8">
    {% for item in site.data.research %}
    <div class="bg-white p-8 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md transition">
      <div class="text-4xl mb-4">{{ item.icon }}</div>
      <h3 class="text-xl font-bold mb-2">{{ item.title }}</h3>
      <p class="text-slate-500 text-sm leading-relaxed">{{ item.description }}</p>
    </div>
    {% endfor %}
  </div>
</section>