---
layout: default
title: 团队成员
---

<section class="bg-white dark:bg-slate-900 border-b border-slate-100 dark:border-slate-800 py-16 transition-colors duration-300 relative z-0">
    <div class="max-w-6xl mx-auto px-4 relative z-10">
        <h1 class="text-4xl font-extrabold text-slate-900 dark:text-white mb-4 tracking-tight transition-colors duration-300">团队成员</h1>
        <p class="text-lg text-slate-500 dark:text-slate-400 max-w-3xl leading-relaxed transition-colors duration-300">
            LV课题组致力于探索真实世界中的智能自主行为。研究领域涵盖多模态感知、3D视觉与具身智能。
        </p>
    </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16">

    <div class="mb-24">
        <div class="flex items-center space-x-4 mb-10 border-l-4 border-blue-600 dark:border-blue-500 pl-4">
            <h2 class="text-2xl font-bold text-slate-800 dark:text-white uppercase tracking-wide transition-colors duration-300">指导教师</h2>
            <span class="text-slate-400 dark:text-slate-500 font-light italic transition-colors duration-300">Faculty</span>
        </div>
        
        <div class="space-y-10">
            {% assign faculty_ids = "professor,associate_prof,assistant_prof,lecturer" | split: "," %}
            {% for f_id in faculty_ids %}
                {% assign teachers = site.data.team | where: "group_id", f_id | sort: "rank" %}
                {% for member in teachers %}
                <div class="bg-white dark:bg-slate-800 rounded-[2.5rem] p-8 md:p-10 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-2xl dark:hover:shadow-blue-900/20 transition-all duration-500 flex flex-col md:flex-row items-center gap-10">
                    <img src="{{ site.baseurl }}{{ member.avatar }}" class="w-48 h-48 md:w-60 md:h-60 rounded-3xl object-cover shadow-xl border-4 border-white dark:border-slate-700 transition-colors duration-300">
                    <div class="flex-1 text-center md:text-left">
                        <div class="mb-4">
                            <span class="role-badge badge-indigo mb-3">{{ member.title }}</span>
                            <h3 class="text-4xl font-bold text-slate-900 dark:text-white mb-2 transition-colors duration-300">{{ member.name }}</h3>
                            <p class="text-blue-600 dark:text-blue-400 font-bold text-xl uppercase tracking-wider transition-colors duration-300">{{ member.role }}</p>
                        </div>
                        <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-6 text-base italic font-light transition-colors duration-300">"{{ member.bio }}"</p>
                        
                        <div class="flex flex-wrap justify-center md:justify-start gap-3 text-sm font-medium">
                            {% if member.email %}
                            <a href="mailto:{{ member.email }}" class="text-slate-500 dark:text-slate-300 bg-slate-50 dark:bg-slate-700/50 hover:bg-blue-50 dark:hover:bg-blue-900/30 hover:text-blue-600 dark:hover:text-blue-400 px-4 py-2 rounded-xl flex items-center gap-2 transition-colors">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                                Email
                            </a>
                            {% endif %}
                            {% if member.links.homepage %}
                            <a href="{{ member.links.homepage }}" target="_blank" class="text-slate-500 dark:text-slate-300 bg-slate-50 dark:bg-slate-700/50 hover:bg-blue-50 dark:hover:bg-blue-900/30 hover:text-blue-600 dark:hover:text-blue-400 px-4 py-2 rounded-xl flex items-center gap-2 transition-colors">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                                个人主页
                            </a>
                            {% endif %}
                            {% if member.links.scholar %}
                            <a href="{{ member.links.scholar }}" target="_blank" class="text-slate-500 dark:text-slate-300 bg-slate-50 dark:bg-slate-700/50 hover:bg-blue-50 dark:hover:bg-blue-900/30 hover:text-blue-600 dark:hover:text-blue-400 px-4 py-2 rounded-xl flex items-center gap-2 transition-colors">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222"></path></svg>
                                Scholar
                            </a>
                            {% endif %}
                            {% if member.links.github %}
                            <a href="{{ member.links.github }}" target="_blank" class="text-slate-500 dark:text-slate-300 bg-slate-50 dark:bg-slate-700/50 hover:bg-slate-200 dark:hover:bg-slate-600 hover:text-slate-900 dark:hover:text-white px-4 py-2 rounded-xl flex items-center gap-2 transition-colors">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
                                GitHub
                            </a>
                            {% endif %}
                        </div>
                    </div>
                </div>
                {% endfor %}
            {% endfor %}
        </div>
    </div>

    <div class="mb-24">
        <div class="flex items-center space-x-4 mb-10 border-l-4 border-blue-400 dark:border-blue-500 pl-4">
            <h2 class="text-2xl font-bold text-slate-800 dark:text-white uppercase tracking-wide transition-colors duration-300">研究生</h2>
            <span class="text-slate-400 dark:text-slate-500 font-light italic transition-colors duration-300">Graduate Students</span>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            {% assign student_ids = "phd,master" | split: "," %}
            {% for s_id in student_ids %}
                {% assign students = site.data.team | where: "group_id", s_id | sort: "rank" %}
                {% for member in students %}
                <div class="group bg-white dark:bg-slate-800 rounded-[2rem] p-8 md:p-10 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-xl dark:hover:shadow-blue-900/20 transition-all flex flex-col sm:flex-row items-start gap-8 min-h-[18rem]">
                    <img src="{{ site.baseurl }}{{ member.avatar }}" class="w-28 h-28 md:w-36 md:h-36 rounded-2xl object-cover shadow-sm group-hover:scale-105 transition-transform flex-shrink-0">
                    
                    <div class="flex-1 flex flex-col h-full min-w-0">
                        <div class="mb-4">
                            <h3 class="text-2xl font-bold text-slate-900 dark:text-white leading-tight transition-colors duration-300">{{ member.name }}</h3>
                            <span class="role-badge {% if s_id == 'phd' %}badge-blue{% else %}badge-cyan{% endif %} mt-2 inline-block">
                                {{ member.title }}
                            </span>
                        </div>
                        <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed mb-6 line-clamp-5 italic flex-grow transition-colors duration-300">"{{ member.bio }}"</p>
                        
                        <div class="grid grid-cols-2 gap-2 mt-auto pt-4 border-t border-slate-50 dark:border-slate-700/50 transition-colors duration-300">
                            {% if member.email %}
                            <a href="mailto:{{ member.email }}" title="{{ member.email }}" class="flex items-center gap-1.5 px-3 py-2 bg-slate-50 dark:bg-slate-700/50 text-slate-500 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/30 rounded-lg text-xs font-medium transition-colors truncate">
                                <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                                <span class="truncate">Email</span>
                            </a>
                            {% endif %}
                            {% if member.links.homepage %}
                            <a href="{{ member.links.homepage }}" target="_blank" class="flex items-center gap-1.5 px-3 py-2 bg-slate-50 dark:bg-slate-700/50 text-slate-500 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/30 rounded-lg text-xs font-medium transition-colors truncate">
                                <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                                <span class="truncate">Homepage</span>
                            </a>
                            {% endif %}
                            {% if member.links.scholar %}
                            <a href="{{ member.links.scholar }}" target="_blank" class="flex items-center gap-1.5 px-3 py-2 bg-slate-50 dark:bg-slate-700/50 text-slate-500 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/30 rounded-lg text-xs font-medium transition-colors truncate">
                                <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222"></path></svg>
                                <span class="truncate">Scholar</span>
                            </a>
                            {% endif %}
                            {% if member.links.github %}
                            <a href="{{ member.links.github }}" target="_blank" class="flex items-center gap-1.5 px-3 py-2 bg-slate-50 dark:bg-slate-700/50 text-slate-500 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-200 dark:hover:bg-slate-600 rounded-lg text-xs font-medium transition-colors truncate">
                                <svg class="w-4 h-4 shrink-0" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
                                <span class="truncate">GitHub</span>
                            </a>
                            {% endif %}
                            {% if member.links.csdn %}
                            <a href="{{ member.links.csdn }}" target="_blank" class="flex items-center gap-1.5 px-3 py-2 bg-slate-50 dark:bg-slate-700/50 text-slate-500 dark:text-slate-300 hover:text-orange-600 dark:hover:text-orange-400 hover:bg-orange-50 dark:hover:bg-orange-900/20 rounded-lg text-xs font-medium transition-colors truncate">
                                <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
                                <span class="truncate">CSDN</span>
                            </a>
                            {% endif %}
                            {% if member.links.zhihu %}
                            <a href="{{ member.links.zhihu }}" target="_blank" class="flex items-center gap-1.5 px-3 py-2 bg-slate-50 dark:bg-slate-700/50 text-slate-500 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/30 rounded-lg text-xs font-medium transition-colors truncate">
                                <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                                <span class="truncate">Zhihu</span>
                            </a>
                            {% endif %}
                        </div>
                    </div>
                </div>
                {% endfor %}
            {% endfor %}
        </div>
    </div>

    <div class="mb-24">
        <div class="flex items-center space-x-4 mb-10 border-l-4 border-green-400 dark:border-green-500 pl-4">
            <h2 class="text-2xl font-bold text-slate-800 dark:text-white uppercase tracking-wide transition-colors duration-300">科研助理与实习生</h2>
            <span class="text-slate-400 dark:text-slate-500 font-light italic transition-colors duration-300">Interns & Assistants</span>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            {% assign intern_ids = "undergrad,interns" | split: "," %}
            {% for i_id in intern_ids %}
                {% assign interns = site.data.team | where: "group_id", i_id %}
                {% for member in interns %}
                <div class="bg-white dark:bg-slate-800 rounded-3xl p-8 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-md transition-colors duration-300 flex flex-col sm:flex-row items-start gap-6 min-h-[14rem]">
                    <img src="{{ site.baseurl }}{{ member.avatar }}" class="w-24 h-24 md:w-28 md:h-28 rounded-2xl object-cover shadow-sm flex-shrink-0">
                    <div class="flex-1 flex flex-col h-full min-w-0">
                        <div class="mb-3">
                            <h3 class="text-xl font-bold text-slate-900 dark:text-white leading-tight transition-colors duration-300">{{ member.name }}</h3>
                            <span class="role-badge badge-green mt-2 inline-block">{{ member.title }}</span>
                        </div>
                        <p class="text-slate-500 dark:text-slate-400 text-xs leading-relaxed mb-5 line-clamp-3 italic flex-grow transition-colors duration-300">"{{ member.bio }}"</p>
                        
                        <div class="grid grid-cols-2 gap-2 mt-auto pt-3 border-t border-slate-50 dark:border-slate-700/50 transition-colors duration-300">
                            {% if member.email %}
                            <a href="mailto:{{ member.email }}" title="{{ member.email }}" class="flex items-center gap-1.5 px-3 py-2 bg-slate-50 dark:bg-slate-700/50 text-slate-500 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/30 rounded-lg text-[0.7rem] font-medium transition-colors truncate">
                                <svg class="w-3.5 h-3.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                                <span class="truncate">Email</span>
                            </a>
                            {% endif %}
                            {% if member.links.homepage %}
                            <a href="{{ member.links.homepage }}" target="_blank" class="flex items-center gap-1.5 px-3 py-2 bg-slate-50 dark:bg-slate-700/50 text-slate-500 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/30 rounded-lg text-[0.7rem] font-medium transition-colors truncate">
                                <svg class="w-3.5 h-3.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                                <span class="truncate">Homepage</span>
                            </a>
                            {% endif %}
                            {% if member.links.github %}
                            <a href="{{ member.links.github }}" target="_blank" class="flex items-center gap-1.5 px-3 py-2 bg-slate-50 dark:bg-slate-700/50 text-slate-500 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-200 dark:hover:bg-slate-600 rounded-lg text-[0.7rem] font-medium transition-colors truncate">
                                <svg class="w-3.5 h-3.5 shrink-0" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
                                <span class="truncate">GitHub</span>
                            </a>
                            {% endif %}
                        </div>
                    </div>
                </div>
                {% endfor %}
            {% endfor %}
        </div>
    </div>

    <div class="mb-12">
        <div class="flex items-center space-x-4 mb-10 border-l-4 border-gray-300 dark:border-gray-600 pl-4">
            <h2 class="text-2xl font-bold text-slate-800 dark:text-white uppercase tracking-wide transition-colors duration-300">往届成员</h2>
            <span class="text-slate-400 dark:text-slate-500 font-light italic transition-colors duration-300">Alumni</span>
        </div>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {% assign alumni = site.data.team | where: "group_id", "alumni" %}
            {% for member in alumni %}
            <div class="group relative bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-lg hover:border-blue-100 dark:hover:border-blue-500 transition-all duration-300 flex flex-col h-full overflow-hidden">
                <div class="absolute top-0 left-0 w-full h-1 bg-slate-100 dark:bg-slate-700 group-hover:bg-blue-400 transition-colors duration-300"></div>
                
                <div class="flex items-center space-x-3 mb-3 mt-1">
                    <div class="w-2.5 h-2.5 rounded-full bg-slate-300 dark:bg-slate-600 group-hover:bg-blue-500 transition-colors"></div>
                    <span class="font-bold text-slate-800 dark:text-white text-lg transition-colors duration-300">{{ member.name }}</span>
                </div>
                
                <p class="text-xs text-slate-500 dark:text-slate-400 mb-5 font-medium tracking-wide uppercase transition-colors duration-300">{{ member.title }}</p>
                
                <div class="mt-auto">
                    <div class="text-xs font-semibold text-blue-700 dark:text-blue-300 bg-blue-50 dark:bg-blue-900/30 border border-blue-100/50 dark:border-blue-800/50 px-3 py-2.5 rounded-xl leading-relaxed transition-colors duration-300">
                        {{ member.destination }}
                    </div>
                </div>

                <div class="absolute bottom-6 right-6 flex space-x-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 translate-y-2 group-hover:translate-y-0">
                    {% if member.links.linkedin %}
                    <a href="{{ member.links.linkedin }}" target="_blank" class="text-slate-400 dark:text-slate-500 hover:text-blue-600 dark:hover:text-blue-400 bg-white dark:bg-slate-700 shadow-sm p-1.5 rounded-md transition-colors" title="LinkedIn">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clip-rule="evenodd"></path></svg>
                    </a>
                    {% endif %}
                    {% if member.links.homepage %}
                    <a href="{{ member.links.homepage }}" target="_blank" class="text-slate-400 dark:text-slate-500 hover:text-blue-600 dark:hover:text-blue-400 bg-white dark:bg-slate-700 shadow-sm p-1.5 rounded-md transition-colors" title="Homepage">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                    </a>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>