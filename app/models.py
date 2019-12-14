from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """
    # 施設名
    F_name = models.CharField(
        verbose_name='施設名',
        max_length=20,
        blank=True,
        null=True,
    )


    # 入力者氏名
    I_name = models.CharField(
        verbose_name='入力者氏名',
        max_length=20,
        blank=True,
        null=True,
    )

    # サンプル項目2 メモ
    memo = models.TextField(
        verbose_name='備考',
        blank=True,
        null=True,
    )

    # サンプル項目3 整数
    quontity = models.IntegerField(
        verbose_name='何kgほしいか',
        blank=True,
        null=True,
    )



    # サンプル項目7 日付
    deadline = models.DateField(
        verbose_name='いつほしいか',
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（固定）
    vege_choice = (
        (1, '人参'),
        (2, '大根'),
        (3, 'じゃがいも'),
        (4, 'キャベツ'),
        (5, 'ホウレンソウ'),
        (6, 'ピーマン'),
        (7, 'なんでもいい'),
    )

    vegetable = models.IntegerField(
        verbose_name='ほしい野菜',
        choices=vege_choice,
        blank=True,
        null=True,
    )

    '''

    # サンプル項目9 選択肢（マスタ連動）
    sample_10 = models.ForeignKey(
        User,
        verbose_name='サンプル項目10_選択肢（マスタ連動）',
        blank=True,
        null=True,
        related_name='sample_10',
        on_delete=models.SET_NULL,
    )

'''

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.sample_1

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
