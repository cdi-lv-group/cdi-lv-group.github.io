---
layout: default
title: 团队成员
---

<section class="bg-white border-b border-slate-100 py-16">
    <div class="max-w-6xl mx-auto px-4">
        <h1 class="text-4xl font-extrabold text-slate-900 mb-4">团队成员</h1>
        <p class="text-lg text-slate-500 max-w-2xl">
            我们是一群专注于多模态感知、3D视觉与具身智能的研究者，致力于探索真实世界中的智能自主行为。
        </p>
    </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-12">
    
    {% for group in site.data.groups %}
        {% assign group_members = site.data.team | where: "group_id", group.id | sort: "rank" %}
        
        {% if group_members.size > 0 %}
            <div class="mb-20">
                <div class="flex items-baseline border-b-2 mb-10 pb-2" style="border-color: #3b82f6;">
                    <h2 class="text-2xl font-bold text-slate-800">{{ group.title }}</h2>
                    <span class="ml-3 text-slate-400 font-light italic">{{ group.subtitle }}</span>
                </div>

                {% if group.id == "professor" or group.id == "associate_prof" or group.id == "assistant_prof" or group.id == "lecturer" %}
                    
                    <div class="space-y-8">
                        {% for member in group_members %}
                        <div class="group bg-white rounded-3xl p-8 border border-slate-100 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col md:flex-row items-start md:items-center gap-8">
                            <img src="{{ site.baseurl }}{{ member.avatar }}" alt="{{ member.name }}" 
                                 class="w-32 h-32 md:w-40 md:h-40 rounded-2xl object-cover border-4 border-slate-50 shadow-sm">
                            
                            <div class="flex-1">
                                <div class="flex flex-wrap items-center gap-3 mb-3">
                                    <h3 class="text-2xl font-bold text-slate-900">{{ member.name }}</h3>
                                    <span class="role-badge badge-{{ group.color }}">{{ member.title }}</span>
                                </div>
                                <p class="text-blue-600 font-semibold mb-3">{{ member.role }}</p>
                                <p class="text-slate-600 text-base leading-relaxed mb-4">
                                    {{ member.bio }}
                                </p>
                                <div class="flex gap-4">
                                    <a href="mailto:{{ member.email }}" class="text-sm text-slate-400 hover:text-blue-600 flex items-center gap-1">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg> Email
                                    </a>
                                    {% if member.link %}
                                    <a href="{{ member.link }}" class="text-sm text-slate-400 hover:text-blue-600 flex items-center gap-1">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg> Homepage
                                    </a>
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>

                {% else %}
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {% for member in group_members %}
                        <div class="bg-white rounded-2xl p-6 border border-slate-100 shadow-sm hover:shadow-md transition-all">
                            <div class="flex items-center space-x-4 mb-4">
                                <img src="{{ site.baseurl }}{{ member.avatar }}" class="w-16 h-16 rounded-full object-cover border-2 border-slate-50">
                                <div>
                                    <h3 class="text-lg font-bold text-slate-900">{{ member.name }}</h3>
                                    <span class="role-badge badge-{{ group.color }} mt-1">{{ member.title }}</span>
                                </div>
                            </div>
                            
                            {% if group.id == "alumni" %}
                                <div class="bg-slate-50 rounded-xl p-3 text-xs text-slate-600 italic">
                                    {{ member.destination }}
                                </div>
                            {% else %}
                                <p class="text-slate-500 text-xs leading-relaxed line-clamp-2 mb-3">{{ member.bio }}</p>
                                <a href="mailto:{{ member.email }}" class="text-xs text-slate-400 hover:text-blue-600 italic">{{ member.email }}</a>
                            {% endif %}
                        </div>
                        {% endfor %}
                    </div>

                {% endif %}
            </div>
        {% endif %}
    {% endfor %}

</section>

<section class="bg-blue-50 py-16">
    <div class="max-w-4xl mx-auto px-4 text-center">
        <h2 class="text-3xl font-bold text-slate-900 mb-4">加入我们</h2>
        <p class="text-slate-600 mb-8">我们常年招收优秀的博士生、硕士生及本科科研实习生。</p>
        <a href="mailto:{{ site.email }}" class="inline-block bg-blue-600 text-white px-8 py-3 rounded-full font-semibold hover:bg-blue-700 transition shadow-lg shadow-blue-200">发送简历</a>
    </div>
</section>