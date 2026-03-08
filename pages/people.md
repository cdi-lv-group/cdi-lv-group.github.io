---
layout: default
title: 团队成员
---

<section class="bg-white dark:bg-slate-900 border-b border-slate-100 dark:border-slate-800 py-16 transition-colors duration-300 relative z-0">
    <div class="max-w-6xl mx-auto px-4 relative z-10">
        <h1 class="text-4xl font-extrabold text-slate-900 dark:text-white mb-4 tracking-tight">
            {% if page.lang == 'en' %}Team Members{% else %}团队成员{% endif %}
        </h1>
        <p class="text-lg text-slate-500 dark:text-slate-400 max-w-3xl leading-relaxed">
            {% if page.lang == 'en' %}
            Exploring intelligent autonomous behavior in the real world through multimodal perception, 3D vision, and embodied intelligence.
            {% else %}
            致力于探索真实世界中的智能自主行为。研究领域涵盖多模态感知、3D视觉与具身智能。
            {% endif %}
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
                    {{ group.title[page.lang] | default: group.title.zh }}
                </h2>
                {% if page.lang == 'zh' %}
                <span class="text-slate-400 dark:text-slate-500 font-light italic ml-2">{{ group.subtitle }}</span>
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
                                    {{ member.title[page.lang] | default: member.title.zh }}
                                </span>
                                <h3 class="text-4xl font-bold text-slate-900 dark:text-white mb-2">
                                    {{ member.name[page.lang] | default: member.name.zh }}
                                </h3>
                                {% if member.role %}
                                <p class="text-{{ group.color }}-600 dark:text-{{ group.color }}-400 font-bold text-xl uppercase tracking-wider">
                                    {{ member.role[page.lang] | default: member.role.zh }}
                                </p>
                                {% endif %}
                            </div>
                            <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-6 text-base italic font-light">
                                "{{ member.bio[page.lang] | default: member.bio.zh }}"
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
                                {{ member.name[page.lang] | default: member.name.zh }}
                            </span>
                        </div>
                        <p class="text-xs text-slate-500 mb-4 uppercase font-medium">
                            {{ member.title[page.lang] | default: member.title.zh }}
                        </p>
                        <div class="mt-auto">
                            <div class="text-xs font-semibold text-{{ group.color }}-700 dark:text-{{ group.color }}-300 bg-{{ group.color }}-50 dark:bg-{{ group.color }}-900/30 px-3 py-2.5 rounded-xl leading-relaxed">
                                {{ member.destination[page.lang] | default: member.destination.zh }}
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
                                {{ member.name[page.lang] | default: member.name.zh }}
                            </h3>
                            <span class="text-xs font-bold text-{{ group.color }}-600 dark:text-{{ group.color }}-400 bg-{{ group.color }}-50 dark:bg-{{ group.color }}-900/20 px-2 py-1 rounded-md uppercase mb-4 inline-block self-start">
                                {{ member.title[page.lang] | default: member.title.zh }}
                            </span>
                            <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed mb-6 italic line-clamp-3 flex-grow">
                                "{{ member.bio[page.lang] | default: member.bio.zh }}"
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