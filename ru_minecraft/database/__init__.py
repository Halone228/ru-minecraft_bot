from peewee import (
    SqliteDatabase,
    Model,
    BigIntegerField,
    TextField
)


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('main.db')


class UserSettings(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    version = TextField(default='')
    mod_type = TextField(default='')


UserSettings.create_table(safe=True)
