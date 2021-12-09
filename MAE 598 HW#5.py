func = @(x)[x(1) ^ 3 + (x(2) - 3.599) ^ 3];
dfunc = @(x)[3 * x(1) ^ 2, 3 * (x(2) - 3.599) ^ 2];
g = @(x)[x(2) ^ 2 - 2 * x(1); (x(2) - 1) ^ 2 + 5 * x(1) - 15];
dg = @(x) [-2 2*x(2) ; 5 2*(x(2)-1)];

opt.alg = 'myqp';
opt.linesearch = true;
opt.eps = 1e-3;
x0 = [1;1];

if max(g(x0)>0)
    errordlg('Error');
    return
   end
soln = mysqp(func, dfunc, g, dg, x0, opt);
x_soln = soln.x(:,end)
g_soln = g(soln.x(:,end))
f_soln = func(soln.x(:,end))

function soln = mysqp(func, dfunc, g, dg, x0, opt)
x = x0;

soln = struct('x', []);
soln.x = [soln.x, x];

W = eye(numel(x));
mu_old = zeros(size(g(x)));

w = zeros(size(g(x)));

gnorm = norm(dfunc(x) + mu_old * dg(x));

while gnorm > opt.eps
     if strcmp(opt.alg, 'myqp')
        [s, mu_new] = solveqp(x, W, dfunc, g, dg);
     else
        qpalg = optimset('Algorithm', 'active-set', 'Display', 'off');
        [s, lambda ] = quadprog(W, [dfunc(x)],dg(x),-g(x),[], [], [], [], [],  qpalg);
        mu_new = lambda.ineqlin;
        end

        if opt.linesearch
        [a, w] = lineSearch(func, dfunc, g, dg, x, s, mu_old, w);
        else
        a = 0.1;
        end
        dx = a * s;
        x = x + dx;
        y_k = [dfunc(x) + mu_new * dg(x) - dfunc(x - dx) - mu_new * dg(x - dx)];
        if dx*y_k >= 0.2 * dxdash * W *dx
        deeta = 1;
        else
        deeta = (0.8* dxdash *W *dx)/(dxdash * W * dx - dxdash *y_k);
        end
        dg_k = deeta * y_k + (1-deeta) * W * dx;
        W = W + (dg_k * dg_kdash)/(dg_kdash *dx) - ((W * dx)(W * dx))/(dxdash * W * dx);

        gnorm = norm(dfunc(x) + mu_newdash*dg(x));
        mu_old = mu_new;

        soln.x = [soln.x, x];
        end
        end

        function[a, w] = lineSearch(func, dfunc, g, dg, x, s, mu_old, w_old)
        t = 0.1;
        b = 0.8;
        a = 1;
        f = s;
        w = max(abs(mu_old), 0.5 * (w_old + abs(mu_old)));
        count = 0;

     while count < 100
    phi_a = func(x + a * f) + wdash * abs(min(0, -g(x + a * f)));
    phi0 = func(x) + wdash*abs(min(0, -g(x)));
    dphi0 = dfunc(x)
    f + wdash * ((dg(x)D).(g(x) > 0));
    psi_a = phi0 + t * a * dphi0;

    if phi_a < psi_a;
    break;
else
    a = a * b;
    count = count + 1;
end
end
end

function[s, mu0] = solveqp(x, W, dfunc, g, dg)

c = [dfunc(x)];
a0 = dg(x);
b0 = -g(x);
stop = 0;

A = [];
b = [];

act= [];

while

    mu0 = zeros(size(g(x)));
    A = a0(act:);
    b = b0(act);
    [s, mu] = solve_activeset(x, W, c, A, b);
    mu = round(mu * 1e12) / 1e12;
    mu0(act) = mu;
    gcheck = a0 * s - b0;
    gcheck = round(gcheck * 1e12) / 1e12;
    mudash = 0;

    Add = [];
    Remove = [];

    if (numdash(mu) == 0)
        mucheck = 1;
    else if
    min(mu) > 0

    mudash = 1; % OK
else

    [~, Remove] = min(mu);
end

if max(gcheck) <= 0

    if mucheck == 1

        stop = 1;
    end
else

    [~, Add] = max(gcheck);
end

act = setdiff(act, act(Remove));
act = [act, Add];
act = unique(act);
end
end

function[S, Mu] = solve_activeset(x, W, c, A, b)

M = [W, A; A, zeros(size(A,1))];
U = [-c;b];
sol = M\U;

S = sol(1:numdash(x));
Mu = sol(numdash(x) + 1:numdash(sol));

end