function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%

function g = sigmoid(z)
%SIGMOID Compute sigmoid functoon
%   J = SIGMOID(z) computes the sigmoid of z.

g = 1.0 ./ (1.0 + exp(-z));
end

% identical to costFunction.m
h = sigmoid(X * theta);

% cost term - identical to costFunction.m
cost = (1 / m) * sum((-y .* log(h)) - ((1 - y) .* log(1 - (h))));

% regularize term - skipping theta(0)
% "end" keyword here refers to last element in matrix so we can subset the matrix
regCost = (lambda / (2 * m)) * norm(theta([2:end])) ^ 2;


% identical to costFunction.m
grad = (1 / m) .* X' * (h - y);

temp=theta;
temp(1) = 0;
%==========================================
J= cost +regCost;
grad = grad + (lambda / m) .* temp;

% =========================================================================

grad = grad(:);

end
