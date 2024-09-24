from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate(self, dados):
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome': 'O nome deve conter apenas letras.'})
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF inválido.'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular': 'O número deve estar de acordo com o modelo a seguir: 99 99999-9999. Utilize adequadamente traço e espaçamento.'})
        return dados
    

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','celular']
    
    def validate(self, dados):
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome': 'O nome deve conter apenas letras.'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular': 'O número deve estar de acordo com o modelo a seguir: 99 99999-9999. Utilize adequadamente traço e espaçamento.'})
        return dados


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class MatriculaPorEstudanteSerializer(serializers.ModelSerializer):
    curso_descricao = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ['curso_descricao', 'periodo',]
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    

class MatriculaPorCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_nome',]