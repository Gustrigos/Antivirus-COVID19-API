from params import *

class Model(object):
  def __init__(self,name,initial_conditions,params,t):
    self.name = name
    self.initial_conditions = initial_conditions
    self.params = params
    self.t = t

  def SEIR(self,theta=1):
    
    initial_conditions = self.initial_conditions
    params = self.params
    t = self.t

    So,Eo,Io,Ro = initial_conditions
    S,E,I,R = [So],[Eo],[Io],[Ro]
    alpha,beta,gamma = params
    dt = t[1]-t[0]
    for _ in t[1:]:
      St = S[-1] - (theta*beta*S[-1]*I[-1])*dt
      Et = E[-1] + (theta*beta*S[-1]*I[-1] - alpha*E[-1])*dt
      It = I[-1] + (alpha*E[-1] - gamma*I[-1])*dt
      Rt = R[-1] + (gamma*I[-1])*dt
      S.append(St)
      E.append(Et)
      I.append(It)
      R.append(Rt)

    return S,E,I,R

  def get_estimates(self):
    S,E,I,R = self.SEIR()

    model_results = {
      'susceptible':S, 
      'exposed':E, 
      'infected':I,
      'recovered':R
    }

    return model_results
 