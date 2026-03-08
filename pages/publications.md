---
layout: default
title: 学术成果
---

<section class="bg-white border-b border-slate-100 py-16">
    <div class="max-w-6xl mx-auto px-4">
        <h1 class="text-4xl font-extrabold text-slate-900 mb-4 tracking-tight">学术成果</h1>
        <p class="text-lg text-slate-500 max-w-3xl leading-relaxed">
            我们在 CVPR, ICCV, NeurIPS 等国际顶级学术会议与期刊上持续发表多模态感知、3D视觉与具身智能领域的研究成果。
        </p>
    </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16 md:py-24">

    {% assign grouped_papers = site.data.publications | group_by: "year" | sort: "name" | reverse %}
    
    {% for year_group in grouped_papers %}
        <div class="mb-20">
            <div class="flex items-center space-x-4 mb-10 border-l-4 border-blue-600 pl-4">
                <h2 class="text-3xl font-black text-slate-800 tracking-tighter">{{ year_group.name }}</h2>
            </div>

            <div class="space-y-10">
                {% for paper in year_group.items %}
                <div class="group bg-white rounded-[2rem] p-6 md:p-8 border border-slate-100 shadow-sm hover:shadow-xl transition-all duration-500 flex flex-col md:flex-row gap-8">
                    
                    {% if paper.image %}
                    <div class="md:w-1/3 flex-shrink-0 overflow-hidden rounded-2xl border border-slate-50 bg-slate-50 relative">
                        <div class="absolute inset-0 bg-blue-900/0 group-hover:bg-blue-900/10 transition-colors duration-500 z-10"></div>
                        <img src="{% if paper.image contains 'http' %}{{ paper.image }}{% else %}{{ site.baseurl }}{{ paper.image }}{% endif %}" 
                             alt="{{ paper.title }}" 
                             class="w-full h-48 md:h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    </div>
                    {% endif %}

                    <div class="flex-1 flex flex-col justify-center">
                        <div class="flex flex-wrap items-center gap-3 mb-3">
                            <span class="inline-block px-3 py-1 bg-slate-100 text-slate-700 text-xs font-bold rounded-md tracking-wide uppercase">
                                {{ paper.venue }}
                            </span>
                            {% if paper.highlight %}
                            <span class="inline-block px-3 py-1 bg-red-50 text-red-600 text-xs font-bold rounded-md tracking-wide uppercase border border-red-100">
                                🔥 {{ paper.highlight }}
                            </span>
                            {% endif %}
                        </div>

                        <h3 class="text-2xl font-bold text-slate-900 leading-snug mb-3 group-hover:text-blue-600 transition-colors">
                            {{ paper.title }}
                        </h3>

                        <p class="text-slate-600 mb-4 text-sm md:text-base leading-relaxed">
                            {{ paper.authors }}
                        </p>

                        {% if paper.abstract %}
                        <p class="text-slate-500 text-sm italic line-clamp-2 mb-6 border-l-2 border-slate-200 pl-3">
                            {{ paper.abstract }}
                        </p>
                        {% endif %}

                        <div class="flex flex-wrap items-center gap-3 mt-auto pt-2">
                            {% if paper.links.paper %}
                            <a href="{{ paper.links.paper }}" target="_blank" class="flex items-center gap-1.5 px-4 py-2 bg-blue-50 text-blue-600 text-sm font-semibold rounded-full hover:bg-blue-600 hover:text-white transition-colors">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                                Paper
                            </a>
                            {% endif %}
                            
                            {% if paper.links.code %}
                            <a href="{{ paper.links.code }}" target="_blank" class="flex items-center gap-1.5 px-4 py-2 bg-slate-800 text-white text-sm font-semibold rounded-full hover:bg-black transition-colors shadow-sm">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
                                Code
                            </a>
                            {% endif %}

                            {% if paper.links.project %}
                            <a href="{{ paper.links.project }}" target="_blank" class="flex items-center gap-1.5 px-4 py-2 bg-slate-50 text-slate-600 text-sm font-semibold rounded-full hover:bg-slate-200 transition-colors">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                                Project Page
                            </a>
                            {% endif %}
                            
                            {% if paper.links.video %}
                            <a href="{{ paper.links.video }}" target="_blank" class="flex items-center gap-1.5 px-4 py-2 bg-red-50 text-red-600 text-sm font-semibold rounded-full hover:bg-red-600 hover:text-white transition-colors">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/></svg>
                                Video
                            </a>
                            {% endif %}
                        </div>

                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    {% endfor %}

</section>

<section class="bg-blue-600 py-16 mb-20 rounded-[3rem] max-w-6xl mx-auto px-4 shadow-xl shadow-blue-100 overflow-hidden relative">
    <div class="absolute top-0 right-0 w-64 h-64 bg-blue-500 rounded-full blur-3xl opacity-20 -mr-20 -mt-20"></div>
    <div class="relative z-10 flex flex-col md:flex-row items-center justify-between text-white md:px-12">
        <div class="mb-8 md:mb-0 text-center md:text-left">
            <h2 class="text-3xl font-bold mb-4">关注我们的开源社区</h2>
            <p class="text-blue-100 max-w-lg">我们坚信开源的力量。实验室的大部分代码与预训练模型都会在 GitHub 上开源，推动 3D 视觉与智能体生态发展。</p>
        </div>
        <div class="flex-shrink-0">
            <a href="{{ site.lab.github }}" target="_blank" class="inline-flex items-center gap-2 bg-white text-blue-600 px-8 py-4 rounded-2xl font-bold hover:bg-blue-50 transition-all shadow-lg hover:-translate-y-1">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
                访问 Lab GitHub
            </a>
        </div>
    </div>
</section>