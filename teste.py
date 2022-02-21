# %%
import boto3

# %%
# teste criado para verificar se as credenciais AWS foram criadas corretamente na máquina
s3 = boto3.resource('s3')
s3.create_bucket(Bucket='bucket-via-boto3')

# %%
