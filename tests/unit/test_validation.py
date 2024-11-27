import pytest
from django.core.exceptions import ValidationError
from elenizado.models import Cours, Video, Categorie
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
class TestModelFieldValidations:

    def test_video_url_validation(self):
        # Test avec une URL invalide
        with pytest.raises(ValidationError):
            video = Video(
                titre="Test Video",
                description="Description test",
                video="invalid_url",
                image=SimpleUploadedFile("test_image.jpg", b"file_content")
            )
            video.full_clean()