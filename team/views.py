from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . forms import UserRegistrationForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from . models import Member
from django.contrib.auth.models import User
from . forms import CreateUserForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def index(request):
    return render(request,"team/index.html")

def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        userEmail = request.POST.get('email')
        username = request.POST.get('username')
        #objects = Member.objects.all()
        # Print all objects
        #for obj in objects:
            #print(obj.email)
        validForm = True
        try:
            memberObject = Member.objects.get(email=userEmail)
        except Member.DoesNotExist:
            form.add_error('email','Could not find the email address in Team database.Please specify the correct one')
            validForm = False
        validForm = validForm and form.is_valid()
        if validForm:
            form.save()
            return render(request,"team/registermessage.html")
    context = {"form": form}
    return render(request,"team/register.html",context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect('listUser')
        else:
            messages.info(request,"Incorrect username or password")

    return render(request,"team/login.html")

def logoutUser(request):
    logout(request)
    return redirect('loginUser')

# function based view
#def listUser(request):
 #   return render(request,'team/member_list.html')

#class based view
class ListUserView(ListView):
    model = Member
    #template_name - member_list
    #context_object_name - object_list 
    paginate_by=5
    #when pagination is specified,the context object is page_obj


# function based view for CreateMember
""" def createUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('listUser')
    context = {"form": form}
    return render(request,"team/createuser.html",context) """

# classbased view for createuser
class CreateUserView(SuccessMessageMixin,CreateView):
    model = Member
    template_name = 'team/createuser.html'
    form_class = CreateUserForm
    success_url = '/listUser/'
    success_message = 'User created successfully'

   # def form_valid(self, form):
       # messages.success(self.request, 'User created successfully')
       # return super().form_valid(form)

#function based view for editMember
""" def editUser(request,pk):
    member = Member.objects.get(id=pk)
    form = CreateUserForm( instance = member)
    loginUserEmail = request.user.email
    isAdminUser = Member.objects.get(email=loginUserEmail).isAdmin
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=member)
        action = request.POST.get('action')
        if action == 'Save':
            if form.is_valid() :
                form.save()
                messages.success(request, 'User updated successfully')
                return redirect('listUser')
        if action == 'Delete':
            member.delete()
            messages.success(request, 'User deleted successfully')
            return redirect('listUser')
    context = {"form": form, "isAdminUser":isAdminUser}
    return render(request,"team/edituser.html",context) """

class EditUserView(UpdateView,DeleteView):
    model = Member
    template_name = 'team/edituser.html'
    form_class = CreateUserForm
    success_url = '/listUser/'

    def form_valid(self, form):
       action = self.request.POST.get('action')
       if action == 'Save':
            self.object.save()
            messages.success(self.request, 'User updated successfully')
       if action == 'Delete':
            deleteUserEmail = self.object.email
            self.object.delete()
            try:
                userObject = User.objects.get(email=deleteUserEmail)
                userObject.delete()
            except User.DoesNotExist:
                print("User deleted in member Database is not present in admin database")
            messages.success(self.request, 'User deleted successfully')
       return redirect('listUser')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loginUserEmail = self.request.user.email
        isAdminUser = False
        try:
            isAdminUser = Member.objects.get(email=loginUserEmail).isAdmin
        except Member.DoesNotExist:
            print("The logged in user is not present in database.This user will considered as superadmin and admin permission will be granted ")
            isAdminUser = True
        context['isAdminUser'] = isAdminUser
        return context

#function based view for deleteMember
#def deleteUser(request,pk):
    #return render(request,'team/member_list.html')