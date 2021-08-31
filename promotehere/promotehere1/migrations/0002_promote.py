# Generated by Django 3.1.2 on 2020-11-25 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotehere1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promote',
            fields=[
                ('promote_id', models.AutoField(primary_key=True, serialize=False)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('fullname', models.CharField(max_length=500)),
                ('user_email', models.CharField(default='', max_length=100)),
                ('user_phone', models.CharField(default='', max_length=100)),
                ('user_promote', models.CharField(default='', max_length=500)),
                ('user_link', models.CharField(default='', max_length=500)),
                ('website_1', models.CharField(default='', max_length=500)),
                ('website_2', models.CharField(default='', max_length=500)),
                ('page_1', models.CharField(default='', max_length=500)),
                ('page_2', models.CharField(default='', max_length=500)),
                ('user_image', models.ImageField(default='', upload_to='promotehere1/images')),
                ('user_moretext', models.CharField(default='', max_length=4000)),
                ('user_add', models.CharField(default='', max_length=4000)),
            ],
        ),
    ]