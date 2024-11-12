#include <bits/stdc++.h>
using namespace std;

float fun_float(float x)
{
    float s = 0;
    s = x * x * x - 2 * x - 5;
    return s;
}


double fun_double(double x)
{
    double s = 0;
    s = x * x * x - 2 * x - 5;
    return s;
}

long double fun_longdouble(long double x)
{
    long double s = 0;
    s = x * x * x - 2 * x - 5;
    return s;
}


int main()
{
    int iteration = 0;
    // freopen("1.out", "w", stdout);
    // Half
    _Float16 x;
    cin >> x;

    
    // Float
    iteration = 0;
    float l2 = 2, r2 = 3, mid2;
    cout << "Float: " << endl;
    while (1)
    {
        iteration++;
        mid2 = (l2 + r2) / 2.0;
        if (fun_float(mid2) == 0) break;
        if (fun_float(l2) * fun_float(mid2) < 0) r2 = mid2;
        else l2 = mid2;
        if (r2 - l2 < 1e-5) break;
        cout << "Iteration: " << iteration << " " << fixed << setprecision(19) << mid2 << "  " << abs(fun_float(mid2)) << endl;
    }
    cout << fixed << setprecision(19) << mid2 << endl;
    cout << endl << endl;

    // Double
    iteration = 0;
    cout << "Double: " << endl; 
    double l3 = 2, r3 = 3, mid3;
    while (1)
    {
        iteration ++;
        mid3 = (l3 + r3) / 2.0;
        if (fun_double(mid3) == 0) break;
        if (fun_double(l3) * fun_double(mid3) < 0) r3 = mid3;
        else l3 = mid3;
        if (r3 - l3 < 1e-15) break;
        cout << "Iteration: " << iteration << " " << fixed << setprecision(19) << mid3 << "  " << abs(fun_float(mid3)) << endl;
    }
    cout << fixed << setprecision(19) << mid3 << endl;
    cout << endl << endl;
    
    // Long Double
    cout << "Long Double: " << endl; 
    long double l4 = 2, r4 = 3, mid4;
    while (1)
    {
        iteration ++;
        mid4 = (l4 + r4) / 2.0;
        if (fun_longdouble(mid4) == 0) break;
        if (fun_double(l4) * fun_double(mid4) < 0) r4 = mid4;
        else l4 = mid4;
        if (r4 - l4 < 1e-18) break;
        cout << "Iteration: " << iteration << " " << fixed << setprecision(19) << mid4 << "  " << abs(fun_float(mid4)) << endl;
    }
    cout << fixed << setprecision(19) << mid4 << endl;
    return 0;
}