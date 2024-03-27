function Guide_Figure_Code(Name, r)
Func = str2func(lower(Name));
Dx = 0:.01:10;
hold on
for x=1:size(r, 1)
    if size(r,2)==2
        rleg(x) = "r = ("+num2str(r(x,1))+", "+num2str(r(x,2))+")";
        plot(Dx, Func(Dx,r(x,:)), LineWidth=2)
    else
        rleg(x) = "r = ("+num2str(r(x))+")";
        plot(Dx, Func(Dx,r(x)), LineWidth=2)
    end

end

axis square
xticks([0,5,10])
yticks([0,.5,1])
xlabel("Distance - x", FontSize=13, FontWeight="bold", FontName="helvetica")
ylabel("Normalized Distance - f(x)", FontSize=13, FontWeight="bold", FontName="helvetica")
title(Name, FontSize=20, FontWeight="bold", FontName="helvetica")
legend(rleg)

end

function [y] = sigmoid(x,r)
if numel(r) == 1
    error('When Fx = "Sigmoid", r must be a two-element vector.')
end
y = 1./(1+exp((x-r(2))/r(1)));
end
function [y] = modsampen(x,r)
if numel(r) == 1
    error('When Fx = "Modsampen", r must be a two-element vector.')
end
y = 1./(1+exp((x-r(2))/r(1)));
end
function [y] = default(x,r)
if numel(r) == 1
    error('When Fx = "Default", r must be a two-element vector.')
end
y = exp(-(x.^r(2))/r(1));
end
function [y] = gudermannian(x,r)
if r <= 0
    error('When Fx = "Gudermannian", r must be a scalar > 0.')
end
y = atan(tanh(r(1)./x));
y = y/max(y);
end

function [y] = triangular(x,r)
    if numel(r) > 1
        error('When Fx = "Triangular", r must be a scalar > 0.')
    end
    y = 1 - (x/r);
    y(x > r) = 0;
end
function [y] = trapezoidal1(x,r)
    if numel(r) > 1
        error('When Fx = "Trapezoidal1", r must be a scalar > 0.')
    end
    y = zeros(size(x));
    y(x <= r*2) = 2 - (x(x <= r*2)/r);
    y(x <= r) = 1;
end
function [y] = trapezoidal2(x,r)
    if numel(r) ~=2 
        error('When Fx = "Trapezoidal2", r must be a two-element vector.')
    end
    y = zeros(size(x));
    y(x <= max(r)) = 1 - (x(x <= max(r))-min(r))/range(r);
    y(x <= min(r)) = 1;
end
function [y] = z_shaped(x, r)
    if numel(r) > 1
        error('When Fx = "Z_shaped", r must be a scalar > 0.')
    end
    y = zeros(size(x));

    y(x <= 2*r) = 2*(((x(x <= 2*r) - 2*r)/r).^2);
    y(x <= 1.5*r) = 1 - (2*(((x(x <= 1.5*r) - r)/r).^2));
    y(x <= r) = 1;
end
function [y] = bell(x, r)
    if numel(r) ~=2 
        error('When Fx = "Bell", r must be a two-element vector.')
    end
    y = 1./(1 + abs(x/r(1)).^(2*r(2)));
end
function [y] = gaussian(x, r)
    if numel(r) > 1
        error('When Fx = "Gaussian", r must be a scalar > 0.')
    end
    y = exp(-((x.^2)/(2*(r^2))));
end
function [y] = constgaussian(x, r)
    if numel(r) > 1
        error('When Fx = "ConstGaussian", r must be a scalar > 0.')
    end
    y = ones(size(x));
    y(x > r) = exp(-log(2)*((x(x > r) - r)/r).^2);
end
