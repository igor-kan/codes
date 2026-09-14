; ModuleID = 'algorithms/02_c/graphs/dijkstra.c'
source_filename = "algorithms/02_c/graphs/dijkstra.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [13 x i8] c"dist[%d]=%d\0A\00", align 1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local void @dijkstra(ptr noundef readonly captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #0 {
  %4 = alloca [100 x i32], align 16
  %5 = alloca [100 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %4) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %5) #6
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(400) %5, i8 0, i64 400, i1 false)
  %6 = icmp sgt i32 %1, 0
  br i1 %6, label %7, label %126

7:                                                ; preds = %3
  %8 = zext nneg i32 %1 to i64
  %9 = icmp ult i32 %1, 8
  br i1 %9, label %20, label %10

10:                                               ; preds = %7
  %11 = and i64 %8, 2147483640
  br label %12

12:                                               ; preds = %12, %10
  %13 = phi i64 [ 0, %10 ], [ %16, %12 ]
  %14 = getelementptr inbounds nuw i32, ptr %4, i64 %13
  %15 = getelementptr inbounds nuw i8, ptr %14, i64 16
  store <4 x i32> splat (i32 2147483647), ptr %14, align 16, !tbaa !5
  store <4 x i32> splat (i32 2147483647), ptr %15, align 16, !tbaa !5
  %16 = add nuw i64 %13, 8
  %17 = icmp eq i64 %16, %11
  br i1 %17, label %18, label %12, !llvm.loop !9

18:                                               ; preds = %12
  %19 = icmp eq i64 %11, %8
  br i1 %19, label %22, label %20

20:                                               ; preds = %7, %18
  %21 = phi i64 [ 0, %7 ], [ %11, %18 ]
  br label %34

22:                                               ; preds = %34, %18
  %23 = sext i32 %2 to i64
  %24 = getelementptr inbounds i32, ptr %4, i64 %23
  store i32 0, ptr %24, align 4, !tbaa !5
  %25 = icmp eq i32 %1, 1
  br i1 %25, label %41, label %26

26:                                               ; preds = %22
  %27 = zext nneg i32 %1 to i64
  %28 = zext nneg i32 %1 to i64
  %29 = add nsw i32 %1, -2
  %30 = and i64 %27, 1
  %31 = and i64 %27, 2147483646
  %32 = icmp eq i64 %30, 0
  %33 = icmp ne i64 %30, 0
  br label %39

34:                                               ; preds = %20, %34
  %35 = phi i64 [ %37, %34 ], [ %21, %20 ]
  %36 = getelementptr inbounds nuw i32, ptr %4, i64 %35
  store i32 2147483647, ptr %36, align 4, !tbaa !5
  %37 = add nuw nsw i64 %35, 1
  %38 = icmp eq i64 %37, %8
  br i1 %38, label %22, label %34, !llvm.loop !13

39:                                               ; preds = %105, %26
  %40 = phi i32 [ 0, %26 ], [ %106, %105 ]
  br label %65

41:                                               ; preds = %105, %22
  %42 = zext nneg i32 %1 to i64
  br label %127

43:                                               ; preds = %100
  br i1 %32, label %59, label %44

44:                                               ; preds = %43
  tail call void @llvm.assume(i1 %33)
  %45 = getelementptr inbounds nuw i32, ptr %5, i64 %102
  %46 = load i32, ptr %45, align 4, !tbaa !5
  %47 = icmp eq i32 %46, 0
  br i1 %47, label %48, label %59

48:                                               ; preds = %44
  %49 = icmp eq i32 %101, -1
  br i1 %49, label %57, label %50

50:                                               ; preds = %48
  %51 = getelementptr inbounds nuw i32, ptr %4, i64 %102
  %52 = load i32, ptr %51, align 4, !tbaa !5
  %53 = sext i32 %101 to i64
  %54 = getelementptr inbounds i32, ptr %4, i64 %53
  %55 = load i32, ptr %54, align 4, !tbaa !5
  %56 = icmp slt i32 %52, %55
  br i1 %56, label %57, label %59

57:                                               ; preds = %50, %48
  %58 = trunc nuw nsw i64 %102 to i32
  br label %59

59:                                               ; preds = %44, %50, %57, %43
  %60 = phi i32 [ %101, %43 ], [ %101, %44 ], [ %58, %57 ], [ %101, %50 ]
  %61 = sext i32 %60 to i64
  %62 = getelementptr inbounds i32, ptr %5, i64 %61
  store i32 1, ptr %62, align 4, !tbaa !5
  %63 = getelementptr inbounds [100 x i32], ptr %0, i64 %61
  %64 = getelementptr inbounds i32, ptr %4, i64 %61
  br label %108

65:                                               ; preds = %100, %39
  %66 = phi i64 [ 0, %39 ], [ %102, %100 ]
  %67 = phi i32 [ -1, %39 ], [ %101, %100 ]
  %68 = phi i64 [ 0, %39 ], [ %103, %100 ]
  %69 = getelementptr inbounds nuw i32, ptr %5, i64 %66
  %70 = load i32, ptr %69, align 8, !tbaa !5
  %71 = icmp eq i32 %70, 0
  br i1 %71, label %72, label %83

72:                                               ; preds = %65
  %73 = icmp eq i32 %67, -1
  br i1 %73, label %81, label %74

74:                                               ; preds = %72
  %75 = getelementptr inbounds nuw i32, ptr %4, i64 %66
  %76 = load i32, ptr %75, align 8, !tbaa !5
  %77 = sext i32 %67 to i64
  %78 = getelementptr inbounds i32, ptr %4, i64 %77
  %79 = load i32, ptr %78, align 4, !tbaa !5
  %80 = icmp slt i32 %76, %79
  br i1 %80, label %81, label %83

81:                                               ; preds = %74, %72
  %82 = trunc nuw nsw i64 %66 to i32
  br label %83

83:                                               ; preds = %65, %74, %81
  %84 = phi i32 [ %67, %65 ], [ %82, %81 ], [ %67, %74 ]
  %85 = or disjoint i64 %66, 1
  %86 = getelementptr inbounds nuw i32, ptr %5, i64 %85
  %87 = load i32, ptr %86, align 4, !tbaa !5
  %88 = icmp eq i32 %87, 0
  br i1 %88, label %89, label %100

89:                                               ; preds = %83
  %90 = icmp eq i32 %84, -1
  br i1 %90, label %98, label %91

91:                                               ; preds = %89
  %92 = getelementptr inbounds nuw i32, ptr %4, i64 %85
  %93 = load i32, ptr %92, align 4, !tbaa !5
  %94 = sext i32 %84 to i64
  %95 = getelementptr inbounds i32, ptr %4, i64 %94
  %96 = load i32, ptr %95, align 4, !tbaa !5
  %97 = icmp slt i32 %93, %96
  br i1 %97, label %98, label %100

98:                                               ; preds = %91, %89
  %99 = trunc nuw nsw i64 %85 to i32
  br label %100

100:                                              ; preds = %98, %91, %83
  %101 = phi i32 [ %84, %83 ], [ %99, %98 ], [ %84, %91 ]
  %102 = add nuw nsw i64 %66, 2
  %103 = add i64 %68, 2
  %104 = icmp eq i64 %103, %31
  br i1 %104, label %43, label %65, !llvm.loop !14

105:                                              ; preds = %123
  %106 = add nuw nsw i32 %40, 1
  %107 = icmp eq i32 %40, %29
  br i1 %107, label %41, label %39, !llvm.loop !15

108:                                              ; preds = %59, %123
  %109 = phi i64 [ 0, %59 ], [ %124, %123 ]
  %110 = getelementptr inbounds nuw i32, ptr %63, i64 %109
  %111 = load i32, ptr %110, align 4, !tbaa !5
  %112 = icmp eq i32 %111, 0
  br i1 %112, label %123, label %113

113:                                              ; preds = %108
  %114 = getelementptr inbounds nuw i32, ptr %5, i64 %109
  %115 = load i32, ptr %114, align 4, !tbaa !5
  %116 = icmp eq i32 %115, 0
  br i1 %116, label %117, label %123

117:                                              ; preds = %113
  %118 = load i32, ptr %64, align 4, !tbaa !5
  %119 = add nsw i32 %118, %111
  %120 = getelementptr inbounds nuw i32, ptr %4, i64 %109
  %121 = load i32, ptr %120, align 4, !tbaa !5
  %122 = tail call i32 @llvm.smin.i32(i32 %119, i32 %121)
  store i32 %122, ptr %120, align 4
  br label %123

123:                                              ; preds = %117, %108, %113
  %124 = add nuw nsw i64 %109, 1
  %125 = icmp eq i64 %124, %28
  br i1 %125, label %105, label %108, !llvm.loop !16

126:                                              ; preds = %127, %3
  call void @llvm.lifetime.end.p0(ptr nonnull %5) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #6
  ret void

127:                                              ; preds = %41, %127
  %128 = phi i64 [ 0, %41 ], [ %133, %127 ]
  %129 = getelementptr inbounds nuw i32, ptr %4, i64 %128
  %130 = load i32, ptr %129, align 4, !tbaa !5
  %131 = trunc nuw nsw i64 %128 to i32
  %132 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %131, i32 noundef %130)
  %133 = add nuw nsw i64 %128, 1
  %134 = icmp eq i64 %133, %42
  br i1 %134, label %126, label %127, !llvm.loop !17
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #2

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #3

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smin.i32(i32, i32) #4

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write)
declare void @llvm.assume(i1 noundef) #5

attributes #0 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #3 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #5 = { nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write) }
attributes #6 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10, !11, !12}
!10 = !{!"llvm.loop.mustprogress"}
!11 = !{!"llvm.loop.isvectorized", i32 1}
!12 = !{!"llvm.loop.unroll.runtime.disable"}
!13 = distinct !{!13, !10, !12, !11}
!14 = distinct !{!14, !10}
!15 = distinct !{!15, !10}
!16 = distinct !{!16, !10}
!17 = distinct !{!17, !10}
