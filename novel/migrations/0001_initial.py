# Generated by Django 4.0.3 on 2022-04-30 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('in_work_space', models.BooleanField(default=True)),
                ('memo', models.CharField(blank=True, max_length=20, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node_author', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='node_parent', to='novel.node')),
                ('voter', models.ManyToManyField(related_name='node_voter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
