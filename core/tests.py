from django.test import TestCase
from core.models import ModelAluno
from core.forms import ModelAlunoForm

# Create your tests here.
class ModelTestCase(TestCase):
    def test_model_creation(self):
        testObject = ModelAluno.objects.create(aluno="Teste123")

        self.assertEqual(testObject.aluno, "Teste123")

class FormTestCase(TestCase):
    def test_valid_form_submission(self):
        form_data = {"aluno": "Teste123", 
                     "professor":"1"}
        
        form = ModelAlunoForm(data=form_data)
        
        self.assertTrue(form.is_valid())

