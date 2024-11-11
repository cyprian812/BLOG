from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers




class CustomRegisterSerializer(RegisterSerializer):
        is_admin = serializers.BooleanField(required=False, default=False)
        is_staff=serializers.BooleanField(required=False)

def save(self, *args, **kwargs):
    # Call the parent save method to create the user instance
    user = super().save(*args, **kwargs)
     # Set the custom field based on the validated data
    user.is_admin = self.validated_data.get('is_blog_admin', False)
    user.is_staff = self.validated_data.get('is_staff', False)
    user.save() # Save the updated user instance
    return user

#     # Set the is_admin field from validated data, defaulting to False if not provided
#     is_admin = self.validated_data.get('is_admin', False)
#     user.is_admin = is_admin

#     # Save the updated user instance with the is_admin attribute
#     user.save()
#     return user  # Return the user instance

# class customregisterserializer(RegisterSerializer):
#       is_staff= serializers.BooleanField(required=False,default=False)
# def save(self, *args, **kwargs):
#     # Call the parent save method to create the user instance
#     user = super().save(*args, **kwargs)
#     is_staff=self.validated_data.get('is_staff',False)



