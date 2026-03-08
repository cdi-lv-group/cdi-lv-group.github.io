---
layout: default
title: 团队成员
---

<section class="bg-white dark:bg-slate-900 border-b border-slate-100 dark:border-slate-800 py-16 md:py-24 transition-colors duration-500 relative overflow-hidden">
    
    <div class="absolute top-0 right-0 -translate-y-1/2 translate-x-1/4 w-96 h-96 bg-blue-50 dark:bg-blue-900/20 rounded-full blur-3xl opacity-50 pointer-events-none"></div>
    <div class="absolute bottom-0 left-0 translate-y-1/2 -translate-x-1/4 w-72 h-72 bg-indigo-50 dark:bg-indigo-900/10 rounded-full blur-3xl opacity-50 pointer-events-none"></div>

    <div class="max-w-6xl mx-auto px-4 relative z-10">
        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-blue-50 dark:bg-blue-900/30 border border-blue-100 dark:border-blue-800 mb-6 transition-all">
            <span class="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
            <span class="text-xs font-bold uppercase tracking-wider text-blue-600 dark:text-blue-400">
                <span class="lang-zh">实验室风采</span>
                <span class="lang-en">Our Talent</span>
            </span>
        </div>

        <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-6 tracking-tight">
            <span class="lang-zh">团队成员</span>
            <span class="lang-en">Team Members</span>
        </h1>

        <p class="text-lg md:text-xl text-slate-500 dark:text-slate-400 max-w-3xl leading-relaxed font-light">
            <span class="lang-zh">
                致力于通过人工智能技术与以人为中心的设计，实现智能体在复杂不确定真实世界中的智能自主行为。主要关注
                <span class="text-blue-600 dark:text-blue-400 font-medium">多模态感知、3D视觉与具身智能</span>。
            </span>
            <span class="lang-en">
                Dedicated to achieving intelligent autonomous behavior in complex environments. Our research focuses on 
                <span class="text-blue-600 dark:text-blue-400 font-medium">multimodal perception, 3D vision, and embodied intelligence</span>.
            </span>
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