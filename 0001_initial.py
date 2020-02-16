# Generated by Django 2.2.6 on 2019-10-24 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fridgehumidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FridgeNumber', models.IntegerField()),
                ('FridgeHumidity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fridgetemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FridgeNumber', models.IntegerField()),
                ('FridgeTemperature', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductPrice', models.IntegerField()),
                ('ProductName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SellerCash', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Phone', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('Flat', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('Pincode', models.IntegerField()),
                ('role', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SellerStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StockQuantity', models.IntegerField()),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sellerstock_requests_created', to='REFridge.Product')),
                ('SellerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sellerstock_requests_created', to='REFridge.Seller')),
            ],
        ),
        migrations.AddField(
            model_name='seller',
            name='UserID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_requests_created', to='REFridge.User1'),
        ),
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FridgeNumber', models.IntegerField()),
                ('FridgeQuantity', models.IntegerField(null=True)),
                ('RequiredLimit', models.IntegerField()),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fridge_requests_created', to='REFridge.Product')),
            ],
            options={
                'unique_together': {('FridgeNumber', 'ProductID')},
            },
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BuyerCash', models.IntegerField()),
                ('Report', models.CharField(max_length=100)),
                ('FridgeStatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer_requests_created', to='REFridge.Fridge')),
                ('UserID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_requests_created', to='REFridge.User1')),
            ],
        ),
        
    ]
