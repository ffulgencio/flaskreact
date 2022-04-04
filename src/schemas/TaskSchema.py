from manage import ma

class TaskSchema(ma.Schema):
    class Meta:
        fields=('id','title', 'description')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)