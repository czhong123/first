# Generated by Django 2.0.4 on 2020-06-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='flavor',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='leixing',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='netcontent',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='packmeth',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='pcount',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='pkind',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='segment',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='segnum',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='specifiactions',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='texture',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='vality',
        ),
        migrations.AddField(
            model_name='detail',
            name='danwei',
            field=models.CharField(max_length=255, null=True, verbose_name='单位'),
        ),
        migrations.AddField(
            model_name='detail',
            name='supplier',
            field=models.CharField(max_length=255, null=True, verbose_name='默认供应商'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='baozhiqi',
            field=models.CharField(max_length=255, null=True, verbose_name='保质期（天）'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='barcode',
            field=models.CharField(max_length=255, null=True, verbose_name='条码'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='brand',
            field=models.CharField(max_length=255, null=True, verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='code1',
            field=models.CharField(max_length=255, null=True, verbose_name='规格值1'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='code2',
            field=models.CharField(max_length=255, null=True, verbose_name='规格值2'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='const1',
            field=models.CharField(max_length=255, null=True, verbose_name='初期成本价'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='fenlei',
            field=models.CharField(max_length=255, null=True, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='heigh',
            field=models.CharField(default='0.0', max_length=255, verbose_name='高度(cm)'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='invendays',
            field=models.CharField(max_length=255, null=True, verbose_name='消耗周期（天）'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='inventory1',
            field=models.CharField(max_length=255, null=True, verbose_name='初期库存'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='invoicename',
            field=models.CharField(max_length=255, null=True, verbose_name='开票名称'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='locatcode',
            field=models.CharField(max_length=255, null=True, verbose_name='货位编码'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='longth',
            field=models.CharField(default='0.0', max_length=255, verbose_name='长度(cm)'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='manufacturer',
            field=models.CharField(max_length=255, null=True, verbose_name='生产商'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='pic1',
            field=models.CharField(max_length=255, null=True, verbose_name='图片1'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='pic2',
            field=models.CharField(max_length=255, null=True, verbose_name='图片2'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='pic3',
            field=models.CharField(max_length=255, null=True, verbose_name='图片3'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='pic4',
            field=models.CharField(max_length=255, null=True, verbose_name='图片4'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='pnumber',
            field=models.CharField(max_length=255, null=True, verbose_name='货号'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='price2',
            field=models.CharField(max_length=255, verbose_name='批发价'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='price3',
            field=models.CharField(max_length=255, verbose_name='参考价'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='price4',
            field=models.CharField(max_length=255, null=True, verbose_name='吊牌价'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='purtype',
            field=models.CharField(max_length=255, null=True, verbose_name='采购类型'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='remarks',
            field=models.CharField(max_length=255, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='skucode',
            field=models.CharField(max_length=255, null=True, verbose_name='规格编码'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='taxrax',
            field=models.CharField(max_length=255, null=True, verbose_name='税率'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='volume',
            field=models.CharField(default='0.0', max_length=255, verbose_name='体积(m^3)'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='weight',
            field=models.CharField(default='0.0', max_length=255, verbose_name='重量(kg)'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='width',
            field=models.CharField(default='0.0', max_length=255, verbose_name='宽度(cm)'),
        ),
    ]
