data <- c="" max=".1),</font" min="0," runif="">
          runif(100000, min=.05, max=.1),
          runif(10000, min=.05, max=1), 
          runif(100000, min=0, max=.2))


slideFunct <- data="" font="" function="" step="" window="">
  total <- data="" font="" length="">
  spots <- -="" 1="" by="step)</font" from="1," seq="" to="(total" window="">
  result <- length="length(spots))</font" vector="">
  for(i in 1:length(spots)){
    result[i] <- -="" 1="" data="" font="" i="" mean="" spots="" window="">
  }
  return(result)
}

