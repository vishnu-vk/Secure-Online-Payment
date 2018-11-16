# Generated by Django 2.1.1 on 2018-10-07 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.FilePathField(path='/home/me/Desktop/p/secure_payment/dataset')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.BigIntegerField()),
                ('holder_name', models.CharField(max_length=50)),
                ('cvv', models.SmallIntegerField()),
                ('exp_month', models.SmallIntegerField()),
                ('exp_year', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cardimage',
            name='card_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cvv_otp_check.CreditCard'),
        ),
    ]