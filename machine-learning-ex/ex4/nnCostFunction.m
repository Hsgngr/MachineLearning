function [J, grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
% add ones (bias) to the first column of X
X = [ones(m, 1), X];
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%
% =========================================================================
% PART 1:

% ======= LAYER 2 =======
% sigmoid input (can be vector or matrix - depending on Theta1)
z2 = X*Theta1';
% activation unit (this can be matrix or vector, depending on output of sigmoid)
a2 = sigmoid(z2);
% add ones to first column of a2
a2 = [ones(m, 1), a2];
% ======= LAYER 3 =======
% sigmoid input (can be vector or matrix - depending on Theta2)
z3 = a2*Theta2';
% activation unit (this can be matrix or vector, depending on output of sigmoid)
a3 = sigmoid(z3);

%%%% ALTERNATIVE FOR LOOP SOLUTION %%%%
% Y_k  = eye(num_labels);
% temp_cost = 0;
% % iterate through all samples and compute cost of each output
% for i = 1:m
%    h_theta = a3(i, :);
%    temp_cost = temp_cost + (log(h_theta)*Y_k(:,y(i)) + log(1-h_theta)*(1-Y_k(:,y(i))));
% end
% J = (-1/m)*temp_cost;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Matrix of all classes -> (m x num_labels)
tmp = eye(num_labels);
Y = (tmp(y,:));
Y_k = Y;

% compute the cost
% INNER sum ouput cost per each y_k_i and h_theta_k(i) ie. per each sample
% on a separate line
% OUTER sum calculates weighted cost across all examples i.e. sums all samples
% and weights them over the number of samples

cost = sum((-Y .* log(a3)) - ((1 - Y) .* log(1 - a3)), 2);
J = (1 / m) * sum(cost);

% compute regularizer
% sum per columns and then per rows of transition matrixes - could be done
% the other way around, too i.e. sum per rows and then per columns
regularizer = (lambda/(2*m))*(sum(sum(Theta1(:,2:end).^2)) + sum(sum(Theta2(:,2:end).^2)));

% resulting regularized cost function
J = J + regularizer;

% -------------------------------------------------------------

% Part 2 - Backpropagation

% pre-allocate matrix for weight deltas - we only have 2 transition matrixes
DELTA_1 = zeros(size(Theta1));
DELTA_2 = zeros(size(Theta2));

for i = 1:m
    x_t = X(i, :);
    y_t = Y_k(i, :);
    
    
    % Forward propagation for (x_t, y_t)
    % ======= LAYER 2 =======
    z2_t = x_t*Theta1';
    a2_t = sigmoid(z2_t);
    % add bias to vector a2_t
    a2_t = [1, a2_t];
    % ======= LAYER 3 =======
    % sigmoid input (can be vector or matrix - depending on Theta2)
    z3_t = a2_t*Theta2';
    % activation unit (this can be matrix or vector, depending on output of sigmoid)
    a3_t = sigmoid(z3_t);
    % compute output error
    delta_3 = (a3_t - y_t);
    % compute hidden layer error
    tmp = Theta2'*delta_3';
    % ignore the bias term and calculate error for layer 2
    delta_2 = tmp(2:end, :)' .* sigmoidGradient(z2_t);
    % Transition matrix error accumulators
    DELTA_1 = DELTA_1 + delta_2'*x_t;
    DELTA_2 = DELTA_2 + delta_3'*a2_t;
end

% don't regularize the bias - we are replacing zero vector in Theta matrix
Theta1_grad = (1/m)*DELTA_1 + (lambda/m)*[zeros(size(Theta1, 1), 1), Theta1(:,2:end)];
Theta2_grad = (1/m)*DELTA_2 + (lambda/m)*[zeros(size(Theta2, 1), 1), Theta2(:,2:end)];

% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];

end