---
layout: default
title: 团队成员
---

<section class="bg-white border-b border-slate-100 py-16">
    <div class="max-w-6xl mx-auto px-4">
        <h1 class="text-4xl font-extrabold text-slate-900 mb-4 tracking-tight">团队成员</h1>
        <p class="text-lg text-slate-500 max-w-3xl leading-relaxed">
            LV课题组致力于探索真实世界中的智能自主行为。研究领域涵盖多模态感知、3D视觉与具身智能。
        </p>
    </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16">

    <div class="mb-24">
        <div class="flex items-center space-x-4 mb-10 border-l-4 border-blue-600 pl-4">
            <h2 class="text-2xl font-bold text-slate-800 uppercase tracking-wide">指导教师</h2>
            <span class="text-slate-400 font-light italic">Faculty</span>
        </div>
        
        <div class="space-y-10">
            {% assign faculty_ids = "professor,associate_prof,assistant_prof,lecturer" | split: "," %}
            {% for f_id in faculty_ids %}
                {% assign teachers = site.data.team | where: "group_id", f_id | sort: "rank" %}
                {% for member in teachers %}
                <div class="bg-white rounded-[2.5rem] p-8 md:p-10 border border-slate-100 shadow-sm hover:shadow-2xl transition-all duration-500 flex flex-col md:flex-row items-center gap-10">
                    <img src="{{ site.baseurl }}{{ member.avatar }}" class="w-48 h-48 md:w-60 md:h-60 rounded-3xl object-cover shadow-xl border-4 border-white">
                    <div class="flex-1 text-center md:text-left">
                        <div class="mb-4">
                            <span class="role-badge badge-indigo mb-3">{{ member.title }}</span>
                            <h3 class="text-4xl font-bold text-slate-900 mb-2">{{ member.name }}</h3>
                            <p class="text-blue-600 font-bold text-xl uppercase tracking-wider">{{ member.role }}</p>
                        </div>
                        <p class="text-slate-600 leading-relaxed mb-6 text-base italic font-light">"{{ member.bio }}"</p>
                        
                        <div class="flex flex-wrap justify-center md:justify-start gap-3 text-sm font-medium">
                            {% if member.email %}
                            <a href="mailto:{{ member.email }}" class="text-slate-500 bg-slate-50 hover:bg-blue-50 hover:text-blue-600 px-3 py-1.5 rounded-lg flex items-center gap-1.5 transition">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                                Email
                            </a>
                            {% endif %}
                            {% if member.links.homepage %}
                            <a href="{{ member.links.homepage }}" target="_blank" class="text-slate-500 bg-slate-50 hover:bg-blue-50 hover:text-blue-600 px-3 py-1.5 rounded-lg flex items-center gap-1.5 transition">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                                主页
                            </a>
                            {% endif %}
                            {% if member.links.scholar %}
                            <a href="{{ member.links.scholar }}" target="_blank" class="text-slate-500 bg-slate-50 hover:bg-blue-50 hover:text-blue-600 px-3 py-1.5 rounded-lg flex items-center gap-1.5 transition">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222"></path></svg>
                                Scholar
                            </a>
                            {% endif %}
                            {% if member.links.github %}
                            <a href="{{ member.links.github }}" target="_blank" class="text-slate-500 bg-slate-50 hover:bg-slate-100 hover:text-slate-900 px-3 py-1.5 rounded-lg flex items-center gap-1.5 transition">
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
        <div class="flex items-center space-x-4 mb-10 border-l-4 border-blue-400 pl-4">
            <h2 class="text-2xl font-bold text-slate-800 uppercase tracking-wide">研究生</h2>
            <span class="text-slate-400 font-light italic">Graduate Students</span>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            {% assign student_ids = "phd,master" | split: "," %}
            {% for s_id in student_ids %}
                {% assign students = site.data.team | where: "group_id", s_id | sort: "rank" %}
                {% for member in students %}
                <div class="group bg-white rounded-3xl p-8 border border-slate-100 shadow-sm hover:shadow-xl transition-all flex flex-col sm:flex-row items-start gap-6 h-full">
                    <img src="{{ site.baseurl }}{{ member.avatar }}" class="w-24 h-24 md:w-28 md:h-28 rounded-2xl object-cover shadow-sm group-hover:scale-105 transition-transform flex-shrink-0">
                    <div class="flex-1 flex flex-col h-full min-w-0">
                        <div class="mb-3">
                            <h3 class="text-xl font-bold text-slate-900 leading-tight">{{ member.name }}</h3>
                            <span class="role-badge {% if s_id == 'phd' %}badge-blue{% else %}badge-cyan{% endif %} mt-2 inline-block">
                                {{ member.title }}
                            </span>
                        </div>
                        <p class="text-slate-500 text-sm leading-relaxed mb-5 line-clamp-4 italic flex-grow">"{{ member.bio }}"</p>
                        
                        <div class="flex flex-wrap items-center gap-4 mt-auto pt-2 border-t border-slate-50">
                            {% if member.email %}
                            <a href="mailto:{{ member.email }}" title="Email: {{ member.email }}" class="text-slate-400 hover:text-blue-600 transition">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                            </a>
                            {% endif %}
                            {% if member.links.homepage %}
                            <a href="{{ member.links.homepage }}" target="_blank" title="个人主页" class="text-slate-400 hover:text-blue-600 transition">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                            </a>
                            {% endif %}
                            {% if member.links.scholar %}
                            <a href="{{ member.links.scholar }}" target="_blank" title="Google Scholar" class="text-slate-400 hover:text-blue-600 transition">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222"></path></svg>
                            </a>
                            {% endif %}
                            {% if member.links.github %}
                            <a href="{{ member.links.github }}" target="_blank" title="GitHub" class="text-slate-400 hover:text-slate-900 transition">
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
                            </a>
                            {% endif %}
                            {% if member.links.csdn %}
                            <a href="{{ member.links.csdn }}" target="_blank" title="CSDN" class="text-slate-400 hover:text-orange-500 transition">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
                            </a>
                            {% endif %}
                            {% if member.links.zhihu %}
                            <a href="{{ member.links.zhihu }}" target="_blank" title="知乎" class="text-slate-400 hover:text-blue-500 transition">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
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
        <div class="flex items-center space-x-4 mb-10 border-l-4 border-green-400 pl-4">
            <h2 class="text-2xl font-bold text-slate-800 uppercase tracking-wide">科研助理与实习生</h2>
            <span class="text-slate-400 font-light italic">Interns & Assistants</span>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            {% assign intern_ids = "undergrad,interns" | split: "," %}
            {% for i_id in intern_ids %}
                {% assign interns = site.data.team | where: "group_id", i_id %}
                {% for member in interns %}
                <div class="bg-white rounded-3xl p-8 border border-slate-100 shadow-sm hover:shadow-md transition-all flex flex-col sm:flex-row items-start gap-6 h-full">
                    <img src="{{ site.baseurl }}{{ member.avatar }}" class="w-20 h-20 md:w-24 md:h-24 rounded-2xl object-cover shadow-sm flex-shrink-0">
                    <div class="flex-1 flex flex-col h-full min-w-0">
                        <div class="mb-3">
                            <h3 class="text-lg font-bold text-slate-900 leading-tight">{{ member.name }}</h3>
                            <span class="role-badge badge-green mt-2 inline-block">{{ member.title }}</span>
                        </div>
                        <p class="text-slate-500 text-xs leading-relaxed mb-5 line-clamp-4 italic flex-grow">"{{ member.bio }}"</p>
                        
                        <div class="flex flex-wrap items-center gap-3 mt-auto pt-2 border-t border-slate-50">
                            {% if member.email %}
                            <a href="mailto:{{ member.email }}" title="Email" class="text-slate-400 hover:text-blue-600 transition">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                            </a>
                            {% endif %}
                            {% if member.links.homepage %}
                            <a href="{{ member.links.homepage }}" target="_blank" title="个人主页" class="text-slate-400 hover:text-blue-600 transition">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                            </a>
                            {% endif %}
                            {% if member.links.github %}
                            <a href="{{ member.links.github }}" target="_blank" title="GitHub" class="text-slate-400 hover:text-slate-900 transition">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
                            </a>
                            {% endif %}
                            {% if member.links.csdn %}
                            <a href="{{ member.links.csdn }}" target="_blank" title="CSDN" class="text-slate-400 hover:text-orange-500 transition">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
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
        <div class="flex items-center space-x-4 mb-10 border-l-4 border-gray-300 pl-4">
            <h2 class="text-2xl font-bold text-slate-800 uppercase tracking-wide">往届成员</h2>
            <span class="text-slate-400 font-light italic">Alumni</span>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
            {% assign alumni = site.data.team | where: "group_id", "alumni" %}
            {% for member in alumni %}
            <div class="group p-5 bg-white border border-slate-100 rounded-2xl hover:border-blue-200 hover:shadow-md transition-all">
                <div class="flex items-center space-x-3 mb-2">
                    <div class="w-2 h-2 rounded-full bg-slate-300 group-hover:bg-blue-400 transition-colors"></div>
                    <span class="font-bold text-slate-800 text-lg">{{ member.name }}</span>
                </div>
                <p class="text-xs text-slate-400 mb-4">{{ member.title }}</p>
                <div class="text-xs font-medium text-blue-700 bg-blue-50 px-3 py-2 rounded-lg leading-relaxed inline-block">
                    {{ member.destination }}
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

</section>

