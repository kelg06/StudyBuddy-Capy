# Generated by Django 5.1.3 on 2025-04-15 15:15

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('days', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='group_flyers/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='app.chat')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_super_admin', models.BooleanField(default=False)),
                ('is_group_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('hometown', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('minor', models.CharField(blank=True, max_length=100, null=True)),
                ('grade', models.CharField(max_length=20)),
                ('grove_or_game_day', models.CharField(choices=[('grove', '📚 The Grove on a quiet day'), ('game_day', '🐅 Game day in the student section')], max_length=50)),
                ('ideal_study_spot', models.CharField(choices=[('ajax', '🍳 Ajax Diner booth'), ('library', '📖 J.D. Williams Library'), ('uptown', '☕ Uptown Coffee'), ('couch', '🏡 My couch')], max_length=50)),
                ('study_time', models.CharField(choices=[('morning', '🌅 Morning'), ('afternoon', '🌞 Afternoon'), ('late_night', '🌙 Late night')], max_length=50)),
                ('energy_source', models.CharField(choices=[('music', '🎧 Music'), ('walks', '🚶 Walks around campus'), ('caffeine', '☕ Caffeine'), ('friends', '👯 Friends')], max_length=50)),
                ('personality_label', models.CharField(choices=[('idea', '💡 Idea person'), ('planner', '📅 Planner'), ('jokester', '🎭 Jokester'), ('deep_thinker', '🧠 Deep thinker')], max_length=50)),
                ('group_project_role', models.CharField(choices=[('lead', '✅ Take the lead'), ('quiet', '✍️ Do the work quietly'), ('organizer', '👥 Organize the group'), ('panic', '😅 Panic last minute (but pull through)')], max_length=50)),
                ('personal_motto', models.CharField(choices=[('work_hard', 'Work hard, play harder'), ('flow', 'Go with the flow'), ('step_by_step', 'One step at a time'), ('done', 'Done is better than perfect')], max_length=50)),
                ('exam_prep_style', models.CharField(choices=[('solo', 'Solo cram session'), ('flashcards', 'Flashcards and repetition'), ('group', 'Group review'), ('teach', 'Teaching someone else')], max_length=50)),
                ('productivity_time', models.CharField(choices=[('morning', '🌅 Morning'), ('afternoon', '🌞 Afternoon'), ('night', '🌙 Night owl'), ('depends', '🌀 Depends on the day')], max_length=50)),
                ('academic_strength', models.CharField(choices=[('detail', '🔍 Focused & detail-oriented'), ('creative', '💭 Creative problem-solver'), ('fast', '🧠 Fast learner'), ('communicator', '💬 Good communicator')], max_length=50)),
                ('accountability_style', models.CharField(choices=[('daily', 'Daily check-ins'), ('deadlines', 'Deadlines & reminders'), ('casual', 'Casual “you good?” texts'), ('self', 'None—I’m self-driven (usually)')], max_length=50)),
                ('weekend_vibe', models.CharField(choices=[('food', '🍽 Trying new food'), ('sports', '🏈 Tailgate or sports'), ('chill', '🧘 Chill & recharge'), ('out', '🎶 Out with friends')], max_length=50)),
                ('meet_people', models.CharField(choices=[('class', 'In class or clubs'), ('greek', 'Greek life events'), ('dm', 'Instagram or DM'), ('random', 'Random convos around campus')], max_length=50)),
                ('wish_more_of', models.CharField(choices=[('time', '⏳ Time'), ('money', '💰 Money'), ('focus', '🧠 Focus'), ('study_buddies', '🙌 Chill people to study with')], max_length=50)),
                ('favorite_tradition', models.CharField(choices=[('grove', '🐅 The Grove'), ('walk', '🔔 Walk of Champions'), ('swayze', '🎉 Swayze student section'), ('fountain', '🎓 Senior fountain jump')], max_length=50)),
                ('hot_take', models.CharField(choices=[('chicken', 'Chicken on a stick > Raising Cane’s'), ('hammocks', 'The Circle should have hammocks'), ('vibes', 'You don’t need a planner — just vibes')], max_length=100)),
                ('secret_campus_hack', models.CharField(max_length=255)),
                ('todays_vibe', models.CharField(choices=[('chill', '😎'), ('sleepy', '😴'), ('overwhelmed', '🤯')], max_length=50)),
                ('planner_fullness', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('social_energy', models.CharField(choices=[('high', '📈'), ('low', '📉'), ('medium', '📊')], max_length=50)),
                ('ghost_likelihood', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=2)),
                ('major_approach', models.CharField(choices=[('love', 'I chose it because I love it'), ('career', 'It aligns with my career goals'), ('realistic', 'It was the most realistic option'), ('figuring_out', 'Still figuring it out 🤷')], max_length=50)),
                ('post_grad_plan', models.CharField(choices=[('grad_school', 'Grad school'), ('job', '💼 Job right away'), ('travel', '✈️ Take time off/travel'), ('unsure', '🤔 Still figuring it out')], max_length=50)),
                ('college_motivation', models.CharField(choices=[('career', '🚀 Career success'), ('learning', '🧠 Learning new stuff'), ('prove', '🧍 Proving it to myself'), ('people', '👫 Meeting the right people')], max_length=50)),
                ('campus_groups', models.CharField(choices=[('fraternity_sorority', '🏛 Fraternity/Sorority'), ('academic_clubs', '🧠 Academic clubs (e.g., Honors College, debate, CME)'), ('creative_orgs', '🎨 Creative orgs (e.g., theatre, film, writing)'), ('sports_intramurals', '🎽 Sports or intramurals'), ('music_arts_groups', '🎸 Music or arts-related groups'), ('class_match_5', 'Class Match 5'), ('religious_orgs', '🙏 Religious orgs (e.g., Cru, Young Life, RUF)'), ('service_groups', '🌍 Service & volunteer groups'), ('niche_clubs', '🧩 Niche interest clubs (e.g., gaming, outdoors, crypto, chess)'), ('not_involved', '🚫 Not involved (yet!)')], max_length=50)),
                ('match_involvement_importance', models.CharField(choices=[('super', 'Super important'), ('little', 'A little'), ('doesnt_matter', 'Doesn’t matter'), ('prefer_not', 'I’d rather they weren’t 🤣')], max_length=50)),
                ('social_energy_on_campus', models.CharField(choices=[('everywhere', 'I’m everywhere — love meeting people'), ('crew', 'I’ve got my crew, but I’m open'), ('low_key', 'Mostly low-key or solo'), ('searching', 'Still trying to find my people')], max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('preferred_gender', models.CharField(blank=True, choices=[('', 'Either'), ('male', 'Male'), ('female', 'Female')], max_length=6, null=True)),
                ('hobbies', models.TextField(blank=True, null=True)),
                ('clubs_and_extracurriculars', models.TextField(blank=True, null=True)),
                ('goals_after', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics/')),
                ('disliked_profiles', models.ManyToManyField(blank=True, related_name='disliked_by', to='app.profile')),
                ('friends', models.ManyToManyField(blank=True, to='app.profile')),
                ('liked_profiles', models.ManyToManyField(blank=True, related_name='liked_by', to='app.profile')),
                ('pending_sent_requests', models.ManyToManyField(blank=True, related_name='pending_received_requests', to='app.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('declined', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_requests', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('sender', 'receiver')},
            },
        ),
    ]
