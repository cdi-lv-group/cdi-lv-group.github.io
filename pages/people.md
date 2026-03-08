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
                        <div class="flex flex-wrap justify-center md:justify-start gap-4 text-sm">
                            <a href="mailto:{{ member.email }}" class="text-slate-400 hover:text-blue-600 flex items-center gap-2">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                                {{ member.email }}
                            </a>
                            {% if member.link %}
                            <a href="{{ member.link }}" class="text-slate-400 hover:text-blue-600 flex items-center gap-2">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                                个人主页
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
                <div class="group bg-white rounded-3xl p-7 border border-slate-100 shadow-sm hover:shadow-xl transition-all flex items-start gap-6">
                    <img src="{{ site.baseurl }}{{ member.avatar }}" class="w-24 h-24 rounded-2xl object-cover shadow-sm group-hover:scale-105 transition-transform">
                    <div class="flex-1 min-w-0">
                        <h3 class="text-xl font-bold text-slate-900 leading-tight">{{ member.name }}</h3>
                        <span class="role-badge {% if s_id == 'phd' %}badge-blue{% else %}badge-cyan{% endif %} mt-2 mb-3">
                            {{ member.title }}
                        </span>
                        <p class="text-slate-500 text-sm leading-relaxed mb-3 line-clamp-2 italic">"{{ member.bio }}"</p>
                        <a href="mailto:{{ member.email }}" class="text-xs text-slate-400 hover:text-blue-600 truncate flex items-center gap-1">
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                            {{ member.email }}
                        </a>
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
                <div class="bg-white rounded-3xl p-7 border border-slate-100 shadow-sm hover:shadow-md transition-all flex items-start gap-6">
                    <img src="{{ site.baseurl }}{{ member.avatar }}" class="w-20 h-20 rounded-2xl object-cover shadow-sm">
                    <div class="flex-1 min-w-0">
                        <h3 class="text-lg font-bold text-slate-900 leading-tight">{{ member.name }}</h3>
                        <span class="role-badge badge-green mt-2 mb-3">{{ member.title }}</span>
                        <p class="text-slate-500 text-xs leading-relaxed line-clamp-2 italic">"{{ member.bio }}"</p>
                        <a href="mailto:{{ member.email }}" class="text-xs text-slate-400 hover:text-blue-600 truncate flex items-center gap-1">
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                            {{ member.email }}
                        </a>
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

<section class="bg-blue-600 py-16 mb-20 rounded-[3rem] max-w-6xl mx-auto px-4 shadow-xl shadow-blue-100 overflow-hidden relative">
    <div class="absolute top-0 right-0 w-64 h-64 bg-blue-500 rounded-full blur-3xl opacity-20 -mr-20 -mt-20"></div>
    <div class="relative z-10 text-center">
        <h2 class="text-3xl font-bold text-white mb-4">加入我们的研究旅程</h2>
        <p class="text-blue-100 mb-10 max-w-2xl mx-auto">我们常年招收有志于人工智能与具身智能研究的优秀学生。如果你也想通过技术探索世界，欢迎加入我们。</p>
        <a href="mailto:{{ site.email }}" class="inline-block bg-white text-blue-600 px-10 py-4 rounded-2xl font-bold hover:bg-blue-50 transition-all shadow-lg">发送简历</a>
    </div>
</section>