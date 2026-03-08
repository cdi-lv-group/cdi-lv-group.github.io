---
layout: default
title: 团队成员
---

<section class="bg-white dark:bg-slate-900 border-b border-slate-100 dark:border-slate-800 py-16 md:py-24 relative overflow-hidden z-0 transition-colors duration-300">
    
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMGg0MHY0MEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGQ9Ik0wIDM5LjVMMDQwIDM5LjUiIHN0cm9rZT0icmdiYSgwLCAwLCAwLCAwLjAzKSIgc3Ryb2tlLXdpZHRoPSIxIi8+PHBhdGggZD0iTTM5LjUgMEwzOS41IDQwIiBzdHJva2U9InJnYmEoMCwgMCwgMCwgMC4wMykiIHN0cm9rZS13aWR0aD0iMSIvPjwvc3ZnPg==')] opacity-60 dark:opacity-10 dark:invert transition-all duration-300 -z-10"></div>
    
    <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-cyan-50 dark:bg-cyan-900/20 rounded-full blur-3xl opacity-60 -translate-y-1/2 translate-x-1/3 transition-colors duration-300 -z-10"></div>
    <div class="absolute bottom-0 left-0 w-[30rem] h-[30rem] bg-blue-50 dark:bg-blue-900/20 rounded-full blur-3xl opacity-40 translate-y-1/3 -translate-x-1/3 transition-colors duration-300 -z-10"></div>
    
    <div class="max-w-6xl mx-auto px-4 relative z-10 text-center md:text-left">
        <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-blue-50 dark:bg-slate-800 border border-blue-100 dark:border-blue-900 text-blue-600 dark:text-blue-400 text-sm font-bold tracking-wide shadow-sm transition-colors duration-300">
            <span class="lang-zh">团队成员</span>
            <span class="lang-en">Team Members</span>
        </div>
        
        <h1 class="text-4xl md:text-6xl font-extrabold text-slate-900 dark:text-white mb-6 tracking-tight leading-tight transition-colors duration-300">
            <span class="lang-zh">凝聚 <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">多元智慧</span> 的核心力量</span>
            <span class="lang-en">The Core Power of <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">Diverse Wisdom</span></span>
        </h1>
        
        <p class="text-lg md:text-xl text-slate-500 dark:text-slate-400 max-w-3xl leading-relaxed font-light mx-auto md:mx-0 transition-colors duration-300">
            <span class="lang-zh">我们的团队由充满激情的跨学科研究者组成。在这里，我们共同打破学术边界，在多模态感知与具身智能领域不断追求卓越，探索真实世界的无限可能。</span>
            <span class="lang-en">Our team consists of passionate interdisciplinary researchers. Here, we break academic boundaries together, pursuing excellence in multimodal perception and embodied AI to explore the infinite possibilities of the real world.</span>
        </p>
    </div>
</section>


<section class="max-w-6xl mx-auto px-4 py-16">
    
    {% for group in site.data.groups %}
        {% assign members = site.data.team | where: "group_id", group.id | sort: "rank" %}
        
        {% if members.size > 0 %}
        <div class="mb-24">
            <div class="flex items-center space-x-4 mb-10 border-l-4 border-{{ group.color }}-500 pl-4">
                <h2 class="text-2xl font-bold text-slate-800 dark:text-white uppercase tracking-wide">
                    <span class="lang-zh">{{ group.title.zh }}</span>
                    <span class="lang-en">{{ group.title.en }}</span>
                </h2>
                {% if group.subtitle %}
                <span class="text-slate-400 dark:text-slate-500 font-light italic ml-2 lang-zh">{{ group.subtitle }}</span>
                {% endif %}
            </div>

            {% if group.id == 'professor' or group.id == 'researchers' %}
                <div class="space-y-10">
                    {% for member in members %}
                    <div class="bg-white dark:bg-slate-800 rounded-[2.5rem] p-8 md:p-10 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-2xl transition-all duration-500 flex flex-col md:flex-row items-center gap-10">
                        <img src="{{ site.baseurl }}{{ member.avatar | default: '/assets/images/team/default_avatar.jpg' }}" class="w-48 h-48 md:w-60 md:h-60 rounded-3xl object-cover shadow-xl border-4 border-white dark:border-slate-700">
                        <div class="flex-1 text-center md:text-left">
                            <div class="mb-4">
                                <span class="px-3 py-1 rounded-full bg-{{ group.color }}-50 dark:bg-{{ group.color }}-900/30 text-{{ group.color }}-600 dark:text-{{ group.color }}-400 text-xs font-bold mb-3 inline-block uppercase tracking-wider">
                                    <span class="lang-zh">{{ member.title.zh }}</span>
                                    <span class="lang-en">{{ member.title.en }}</span>
                                </span>
                                <h3 class="text-4xl font-bold text-slate-900 dark:text-white mb-2">
                                    <span class="lang-zh">{{ member.name.zh }}</span>
                                    <span class="lang-en">{{ member.name.en }}</span>
                                </h3>
                                {% if member.role %}
                                <p class="text-{{ group.color }}-600 dark:text-{{ group.color }}-400 font-bold text-xl uppercase tracking-wider">
                                    <span class="lang-zh">{{ member.role.zh }}</span>
                                    <span class="lang-en">{{ member.role.en }}</span>
                                </p>
                                {% endif %}
                            </div>
                            <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-6 text-base italic font-light">
                                <span class="lang-zh">"{{ member.bio.zh }}"</span>
                                <span class="lang-en">"{{ member.bio.en }}"</span>
                            </p>
                            
                            <div class="flex flex-wrap justify-center md:justify-start gap-3">
                                {% include team-links.html links=member.links email=member.email color=group.color %}
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>

            {% elsif group.id == 'alumni' %}
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    {% for member in members %}
                    <div class="group relative bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-lg transition-all flex flex-col h-full">
                        <div class="flex items-center space-x-3 mb-2">
                            <div class="w-2 h-2 rounded-full bg-{{ group.color }}-400"></div>
                            <span class="font-bold text-slate-800 dark:text-white text-lg">
                                <span class="lang-zh">{{ member.name.zh }}</span>
                                <span class="lang-en">{{ member.name.en }}</span>
                            </span>
                        </div>
                        <p class="text-xs text-slate-500 mb-4 uppercase font-medium">
                            <span class="lang-zh">{{ member.title.zh }}</span>
                            <span class="lang-en">{{ member.title.en }}</span>
                        </p>
                        <div class="mt-auto">
                            <div class="text-xs font-semibold text-{{ group.color }}-700 dark:text-{{ group.color }}-300 bg-{{ group.color }}-50 dark:bg-{{ group.color }}-900/30 px-3 py-2.5 rounded-xl leading-relaxed">
                                <span class="lang-zh">{{ member.destination.zh }}</span>
                                <span class="lang-en">{{ member.destination.en }}</span>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>

            {% else %}
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    {% for member in members %}
                    <div class="group bg-white dark:bg-slate-800 rounded-[2rem] p-8 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-xl transition-all flex flex-col sm:flex-row gap-8">
                        <img src="{{ site.baseurl }}{{ member.avatar | default: '/assets/images/team/default_avatar.jpg' }}" class="w-28 h-28 md:w-32 md:h-32 rounded-2xl object-cover shrink-0 group-hover:scale-105 transition-transform">
                        <div class="flex-1 flex flex-col">
                            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-1">
                                <span class="lang-zh">{{ member.name.zh }}</span>
                                <span class="lang-en">{{ member.name.en }}</span>
                            </h3>
                            <span class="text-xs font-bold text-{{ group.color }}-600 dark:text-{{ group.color }}-400 bg-{{ group.color }}-50 dark:bg-{{ group.color }}-900/20 px-2 py-1 rounded-md uppercase mb-4 inline-block self-start">
                                <span class="lang-zh">{{ member.title.zh }}</span>
                                <span class="lang-en">{{ member.title.en }}</span>
                            </span>
                            <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed mb-6 italic line-clamp-3 flex-grow">
                                <span class="lang-zh">"{{ member.bio.zh }}"</span>
                                <span class="lang-en">"{{ member.bio.en }}"</span>
                            </p>
                            <div class="flex flex-wrap gap-2 mt-auto">
                                {% include team-links.html links=member.links email=member.email color=group.color small=true %}
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            {% endif %}
        </div>
        {% endif %}
    {% endfor %}
</section>