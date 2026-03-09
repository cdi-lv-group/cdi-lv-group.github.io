---
layout: default
title: 学术成果
---

<section class="bg-white dark:bg-slate-900 border-b border-slate-100 dark:border-slate-800 py-20 md:py-28 relative overflow-hidden z-0 transition-colors duration-300">
    
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMGg0MHY0MEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGQ9Ik0wIDM5LjVMMDQwIDM5LjUiIHN0cm9rZT0icmdiYSgwLCAwLCAwLCAwLjAzKSIgc3Ryb2tlLXdpZHRoPSIxIi8+PHBhdGggZD0iTTM5LjUgMEwzOS41IDQwIiBzdHJva2U9InJnYmEoMCwgMCwgMCwgMC4wMykiIHN0cm9rZS13aWR0aD0iMSIvPjwvc3ZnPg==')] opacity-60 dark:opacity-10 dark:invert transition-all duration-300 -z-10"></div>
    
    <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-blue-50 dark:bg-blue-900/20 rounded-full blur-3xl opacity-60 -translate-y-1/2 translate-x-1/3 transition-colors duration-300 -z-10"></div>
    <div class="absolute bottom-0 left-0 w-[30rem] h-[30rem] bg-cyan-50 dark:bg-cyan-900/10 rounded-full blur-3xl opacity-40 translate-y-1/3 -translate-x-1/4 transition-colors duration-300 -z-10"></div>

    <div class="max-w-6xl mx-auto px-4 relative z-10 text-center md:text-left">
        
        <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-blue-50 dark:bg-slate-800 border border-blue-100 dark:border-blue-900 text-blue-600 dark:text-blue-400 text-sm font-bold tracking-wide shadow-sm transition-colors duration-300">
            <span class="lang-zh">{{ site.publications_header.badge.zh }}</span>
            <span class="lang-en">{{ site.publications_header.badge.en }}</span>
        </div>

        <h1 class="text-4xl md:text-6xl font-extrabold text-slate-900 dark:text-white mb-6 tracking-tight leading-tight transition-colors duration-300">
            <span class="lang-zh">
                {{ site.publications_header.title_main.zh }}<br class="block md:hidden"/>
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">{{ site.publications_header.title_gradient.zh }}</span>
            </span>
            <span class="lang-en">
                {{ site.publications_header.title_main.en }}<br class="block md:hidden"/>
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">{{ site.publications_header.title_gradient.en }}</span>
            </span>
        </h1>
        
        <p class="text-lg md:text-xl text-slate-500 dark:text-slate-400 max-w-3xl mx-auto md:mx-0 leading-relaxed font-light transition-colors duration-300">
            <span class="lang-zh">{{ site.publications_header.description.zh }}</span>
            <span class="lang-en">{{ site.publications_header.description.en }}</span>
        </p>
    </div>
</section>


<section class="max-w-6xl mx-auto px-4 py-16 md:py-24">

    {% assign grouped_papers = site.data.publications | group_by: "year" | sort: "name" | reverse %}
    
    {% for year_group in grouped_papers %}
        <div class="mb-20">
            <div class="flex items-center space-x-4 mb-10 border-l-4 border-blue-600 dark:border-blue-500 pl-4">
                <h2 class="text-3xl font-black text-slate-800 dark:text-white tracking-tighter transition-colors duration-300">{{ year_group.name }}</h2>
            </div>

            <div class="space-y-10">
                {% for paper in year_group.items %}
                <div class="group bg-white dark:bg-slate-800 rounded-[2rem] p-6 md:p-8 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-xl dark:hover:shadow-blue-900/20 transition-all duration-500 flex flex-col md:flex-row gap-8">
                    
                    {% if paper.image %}
                    <div class="md:w-1/3 flex-shrink-0 overflow-hidden rounded-2xl border border-slate-50 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 relative transition-colors duration-300">
                        <div class="absolute inset-0 bg-blue-900/0 group-hover:bg-blue-900/10 dark:group-hover:bg-white/5 transition-colors duration-500 z-10"></div>
                        <img src="{% if paper.image contains 'http' %}{{ paper.image }}{% else %}{{ site.baseurl }}{{ paper.image }}{% endif %}" 
                             alt="{{ paper.title.zh | default: paper.title }}" 
                             class="w-full h-48 md:h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    </div>
                    {% endif %}

                    <div class="flex-1 flex flex-col justify-center">
                        <div class="flex flex-wrap items-center gap-3 mb-3">
                            
                            {% if paper.type == "journal" %}
                                <span class="inline-block px-3 py-1 bg-green-50 dark:bg-green-900/30 text-green-600 dark:text-green-400 text-xs font-bold rounded-md tracking-wide uppercase transition-colors duration-300">Journal</span>
                            {% elsif paper.type == "preprint" %}
                                <span class="inline-block px-3 py-1 bg-slate-100 dark:bg-slate-700 text-slate-500 dark:text-slate-400 text-xs font-bold rounded-md tracking-wide uppercase transition-colors duration-300">Preprint</span>
                            {% elsif paper.type == "conference" %}
                                <span class="inline-block px-3 py-1 bg-indigo-50 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400 text-xs font-bold rounded-md tracking-wide uppercase transition-colors duration-300">Conference</span>
                            {% endif %}

                            <span class="inline-block px-3 py-1 bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-300 text-xs font-bold rounded-md tracking-wide uppercase transition-colors duration-300">
                                <span class="lang-zh">{{ paper.venue.zh | default: paper.venue }}</span>
                                <span class="lang-en">{{ paper.venue.en | default: paper.venue }}</span>
                            </span>
                            
                            {% if paper.highlight and paper.highlight != "" %}
                            <span class="inline-block px-3 py-1 bg-red-50 dark:bg-red-900/30 text-red-600 dark:text-red-400 text-xs font-bold rounded-md tracking-wide uppercase border border-red-100 dark:border-red-800/50 transition-colors duration-300">
                                🔥 
                                <span class="lang-zh">{{ paper.highlight.zh | default: paper.highlight }}</span>
                                <span class="lang-en">{{ paper.highlight.en | default: paper.highlight }}</span>
                            </span>
                            {% endif %}
                        </div>

                        <h3 class="text-2xl font-bold text-slate-900 dark:text-white leading-snug mb-3 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors duration-300">
                            <span class="lang-zh">{{ paper.title.zh | default: paper.title }}</span>
                            <span class="lang-en">{{ paper.title.en | default: paper.title }}</span>
                        </h3>

                        <p class="text-slate-600 dark:text-slate-300 mb-4 text-sm md:text-base leading-relaxed transition-colors duration-300">
                            {{ paper.authors }}
                        </p>

                        {% if paper.abstract %}
                        <p class="text-slate-500 dark:text-slate-400 text-sm italic line-clamp-2 mb-6 border-l-2 border-slate-200 dark:border-slate-600 pl-3 transition-colors duration-300">
                            <span class="lang-zh">{{ paper.abstract.zh | default: paper.abstract }}</span>
                            <span class="lang-en">{{ paper.abstract.en | default: paper.abstract }}</span>
                        </p>
                        {% endif %}

                        <div class="flex flex-wrap items-center gap-3 mt-auto pt-2">
                            {% if paper.links.paper and paper.links.paper != "" and paper.links.paper != "#" %}
                            <a href="{{ paper.links.paper }}" target="_blank" class="flex items-center gap-1.5 px-4 py-2 bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400 text-sm font-semibold rounded-full hover:bg-blue-600 dark:hover:bg-blue-500 hover:text-white dark:hover:text-white transition-colors">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                                Paper
                            </a>
                            {% endif %}
                            
                            {% if paper.links.code and paper.links.code != "" and paper.links.code != "#" %}
                            <a href="{{ paper.links.code }}" target="_blank" class="flex items-center gap-1.5 px-4 py-2 bg-slate-800 dark:bg-slate-700 text-white text-sm font-semibold rounded-full hover:bg-black dark:hover:bg-slate-600 transition-colors shadow-sm">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
                                Code
                            </a>
                            {% endif %}

                            {% if paper.links.project and paper.links.project != "" and paper.links.project != "#" %}
                            <a href="{{ paper.links.project }}" target="_blank" class="flex items-center gap-1.5 px-4 py-2 bg-slate-50 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300 text-sm font-semibold rounded-full hover:bg-slate-200 dark:hover:bg-slate-600 transition-colors">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                                Project
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

<section class="bg-blue-600 dark:bg-slate-800 py-16 mb-20 rounded-[3rem] max-w-6xl mx-auto px-4 shadow-xl shadow-blue-100 dark:shadow-none border dark:border-slate-700 overflow-hidden relative transition-colors duration-300">
    <div class="absolute top-0 right-0 w-64 h-64 bg-blue-500 dark:bg-slate-700 rounded-full blur-3xl opacity-20 dark:opacity-30 -mr-20 -mt-20 transition-colors duration-300"></div>
    
    <div class="relative z-10 flex flex-col md:flex-row items-center justify-between text-white md:px-12">
        <div class="mb-8 md:mb-0 text-center md:text-left">
            <h2 class="text-3xl font-bold mb-4">
                <span class="lang-zh">关注我们的开源社区</span>
                <span class="lang-en">Join Our Open Source Community</span>
            </h2>
            <p class="text-blue-100 dark:text-slate-300 max-w-lg transition-colors duration-300">
                <span class="lang-zh">我们坚信开源的力量。实验室的大部分代码与预训练模型都会在 GitHub 上开源，推动 3D 视觉与智能体生态发展。</span>
                <span class="lang-en">We believe in the power of open source. Most of our code and pre-trained models are released on GitHub to advance the 3D vision and embodied AI ecosystem.</span>
            </p>
        </div>
        <div class="flex-shrink-0">
            <a href="{{ site.lab.github }}" target="_blank" class="inline-flex items-center gap-2 bg-white dark:bg-blue-600 text-blue-600 dark:text-white px-8 py-4 rounded-2xl font-bold hover:bg-blue-50 dark:hover:bg-blue-500 transition-all shadow-lg hover:-translate-y-1">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
                <span class="lang-zh">访问 Lab GitHub</span>
                <span class="lang-en">Visit Lab GitHub</span>
            </a>
        </div>
    </div>
</section>