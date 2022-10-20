# Generated by Django 4.0.5 on 2022-10-19 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0003_alter_billinglocation_request_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billinglocation',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='order_app.order'),
        ),
        migrations.AlterField(
            model_name='billinglocation',
            name='request_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('success', 'Accepted'), ('delivered', 'Delivered'), ('failed', 'Rejected'), ('cancelled', 'Cancelled'), ('pending', 'Pending')], default='pending', max_length=20),
        ),
    ]
