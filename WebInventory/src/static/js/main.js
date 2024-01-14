var a;
function pass()
{
    if (a==1)
    {
        document.getElementById('password').type='password';
        document.getElementById('show-password').type='checkbox';
        a=0;
    }
    else
    {
        document.getElementById('password').type='text';
        document.getElementById('show-password').type='checkbox';
        a=1;
    }
}