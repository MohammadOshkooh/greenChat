# Generated by Django 4.1 on 2022-08-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_chat_link_remove_contactlist_contact_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Received_from_the_group',
            new_name='received_from_the_group',
        ),
        migrations.AlterField(
            model_name='chat',
            name='link',
            field=models.CharField(default='sHWzbrRlVEyo4G6suNgq', max_length=50, unique=True),
        ),
    ]
