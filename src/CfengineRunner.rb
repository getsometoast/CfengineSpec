module CfengineSpec
  class CfengineRunner
    def self.RunAgentForPromise(promise)
      output = `cf-agent --dry-run -v #{promise}`
      return CfengineRunnerResult.build_from_verbose_output(output)
    end
  end
end
