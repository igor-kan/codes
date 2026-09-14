; ModuleID = 'algorithms/02_c/sorting/counting_sort.c'
source_filename = "algorithms/02_c/sorting/counting_sort.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@__const.main.data = private unnamed_addr constant [10 x i32] [i32 5, i32 3, i32 8, i32 1, i32 9, i32 2, i32 7, i32 4, i32 6, i32 0], align 16
@.str = private unnamed_addr constant [49 x i8] c"[C CountingSort] FAILED: not sorted at index %d\0A\00", align 1
@.str.1 = private unnamed_addr constant [43 x i8] c"[C CountingSort] Counting sort verified: {\00", align 1
@.str.2 = private unnamed_addr constant [5 x i8] c"%d%s\00", align 1
@.str.3 = private unnamed_addr constant [3 x i8] c", \00", align 1
@.str.4 = private unnamed_addr constant [3 x i8] c"}\0A\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @counting_sort(ptr noundef captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #0 {
  %4 = alloca [1000001 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %4) #7
  %5 = add i32 %2, 1
  %6 = sext i32 %5 to i64
  %7 = shl nsw i64 %6, 2
  call void @llvm.memset.p0.i64(ptr nonnull align 16 %4, i8 0, i64 %7, i1 false)
  %8 = icmp sgt i32 %1, 0
  br i1 %8, label %9, label %32

9:                                                ; preds = %3
  %10 = zext nneg i32 %1 to i64
  %11 = and i64 %10, 3
  %12 = icmp ult i32 %1, 4
  br i1 %12, label %17, label %13

13:                                               ; preds = %9
  %14 = and i64 %10, 2147483644
  br label %36

15:                                               ; preds = %36
  %16 = icmp eq i64 %11, 0
  br i1 %16, label %32, label %17

17:                                               ; preds = %15, %9
  %18 = phi i64 [ 0, %9 ], [ %66, %15 ]
  %19 = icmp ne i64 %11, 0
  tail call void @llvm.assume(i1 %19)
  br label %20

20:                                               ; preds = %20, %17
  %21 = phi i64 [ %18, %17 ], [ %29, %20 ]
  %22 = phi i64 [ 0, %17 ], [ %30, %20 ]
  %23 = getelementptr inbounds nuw i32, ptr %0, i64 %21
  %24 = load i32, ptr %23, align 4, !tbaa !5
  %25 = sext i32 %24 to i64
  %26 = getelementptr inbounds i32, ptr %4, i64 %25
  %27 = load i32, ptr %26, align 4, !tbaa !5
  %28 = add nsw i32 %27, 1
  store i32 %28, ptr %26, align 4, !tbaa !5
  %29 = add nuw nsw i64 %21, 1
  %30 = add i64 %22, 1
  %31 = icmp eq i64 %30, %11
  br i1 %31, label %32, label %20, !llvm.loop !9

32:                                               ; preds = %15, %20, %3
  %33 = icmp slt i32 %2, 0
  br i1 %33, label %100, label %34

34:                                               ; preds = %32
  %35 = zext i32 %5 to i64
  br label %69

36:                                               ; preds = %36, %13
  %37 = phi i64 [ 0, %13 ], [ %66, %36 ]
  %38 = phi i64 [ 0, %13 ], [ %67, %36 ]
  %39 = getelementptr inbounds nuw i32, ptr %0, i64 %37
  %40 = load i32, ptr %39, align 4, !tbaa !5
  %41 = sext i32 %40 to i64
  %42 = getelementptr inbounds i32, ptr %4, i64 %41
  %43 = load i32, ptr %42, align 4, !tbaa !5
  %44 = add nsw i32 %43, 1
  store i32 %44, ptr %42, align 4, !tbaa !5
  %45 = getelementptr inbounds nuw i32, ptr %0, i64 %37
  %46 = getelementptr inbounds nuw i8, ptr %45, i64 4
  %47 = load i32, ptr %46, align 4, !tbaa !5
  %48 = sext i32 %47 to i64
  %49 = getelementptr inbounds i32, ptr %4, i64 %48
  %50 = load i32, ptr %49, align 4, !tbaa !5
  %51 = add nsw i32 %50, 1
  store i32 %51, ptr %49, align 4, !tbaa !5
  %52 = getelementptr inbounds nuw i32, ptr %0, i64 %37
  %53 = getelementptr inbounds nuw i8, ptr %52, i64 8
  %54 = load i32, ptr %53, align 4, !tbaa !5
  %55 = sext i32 %54 to i64
  %56 = getelementptr inbounds i32, ptr %4, i64 %55
  %57 = load i32, ptr %56, align 4, !tbaa !5
  %58 = add nsw i32 %57, 1
  store i32 %58, ptr %56, align 4, !tbaa !5
  %59 = getelementptr inbounds nuw i32, ptr %0, i64 %37
  %60 = getelementptr inbounds nuw i8, ptr %59, i64 12
  %61 = load i32, ptr %60, align 4, !tbaa !5
  %62 = sext i32 %61 to i64
  %63 = getelementptr inbounds i32, ptr %4, i64 %62
  %64 = load i32, ptr %63, align 4, !tbaa !5
  %65 = add nsw i32 %64, 1
  store i32 %65, ptr %63, align 4, !tbaa !5
  %66 = add nuw nsw i64 %37, 4
  %67 = add i64 %38, 4
  %68 = icmp eq i64 %67, %14
  br i1 %68, label %15, label %36, !llvm.loop !11

69:                                               ; preds = %34, %111
  %70 = phi i64 [ 0, %34 ], [ %114, %111 ]
  %71 = phi i32 [ 0, %34 ], [ %113, %111 ]
  %72 = getelementptr inbounds nuw i32, ptr %4, i64 %70
  %73 = load i32, ptr %72, align 4, !tbaa !5
  %74 = add nsw i32 %73, -1
  %75 = icmp sgt i32 %73, 0
  br i1 %75, label %76, label %111

76:                                               ; preds = %69
  %77 = sext i32 %71 to i64
  %78 = trunc nuw nsw i64 %70 to i32
  %79 = zext nneg i32 %73 to i64
  %80 = icmp ult i32 %73, 8
  br i1 %80, label %97, label %81

81:                                               ; preds = %76
  %82 = and i64 %79, 2147483640
  %83 = add nsw i64 %82, %77
  %84 = trunc nuw nsw i64 %82 to i32
  %85 = sub i32 %74, %84
  %86 = insertelement <4 x i32> poison, i32 %78, i64 0
  %87 = shufflevector <4 x i32> %86, <4 x i32> poison, <4 x i32> zeroinitializer
  %88 = getelementptr i32, ptr %0, i64 %77
  br label %89

89:                                               ; preds = %89, %81
  %90 = phi i64 [ 0, %81 ], [ %93, %89 ]
  %91 = getelementptr i32, ptr %88, i64 %90
  %92 = getelementptr inbounds nuw i8, ptr %91, i64 16
  store <4 x i32> %87, ptr %91, align 4, !tbaa !5
  store <4 x i32> %87, ptr %92, align 4, !tbaa !5
  %93 = add nuw i64 %90, 8
  %94 = icmp eq i64 %93, %82
  br i1 %94, label %95, label %89, !llvm.loop !13

95:                                               ; preds = %89
  %96 = icmp eq i64 %82, %79
  br i1 %96, label %108, label %97

97:                                               ; preds = %76, %95
  %98 = phi i64 [ %77, %76 ], [ %83, %95 ]
  %99 = phi i32 [ %74, %76 ], [ %85, %95 ]
  br label %101

100:                                              ; preds = %111, %32
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #7
  ret void

101:                                              ; preds = %97, %101
  %102 = phi i64 [ %104, %101 ], [ %98, %97 ]
  %103 = phi i32 [ %106, %101 ], [ %99, %97 ]
  %104 = add nsw i64 %102, 1
  %105 = getelementptr inbounds i32, ptr %0, i64 %102
  store i32 %78, ptr %105, align 4, !tbaa !5
  %106 = add nsw i32 %103, -1
  %107 = icmp eq i32 %103, 0
  br i1 %107, label %108, label %101, !llvm.loop !16

108:                                              ; preds = %101, %95
  %109 = phi i64 [ %83, %95 ], [ %104, %101 ]
  %110 = trunc nsw i64 %109 to i32
  br label %111

111:                                              ; preds = %108, %69
  %112 = phi i32 [ %74, %69 ], [ -1, %108 ]
  %113 = phi i32 [ %71, %69 ], [ %110, %108 ]
  store i32 %112, ptr %72, align 4, !tbaa !5
  %114 = add nuw nsw i64 %70, 1
  %115 = icmp eq i64 %114, %35
  br i1 %115, label %100, label %69, !llvm.loop !17
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #2

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #3 {
  %1 = alloca [1000001 x i32], align 16
  %2 = alloca [10 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #7
  call void @llvm.memcpy.p0.p0.i64(ptr noundef nonnull align 16 dereferenceable(40) %2, ptr noundef nonnull align 16 dereferenceable(40) @__const.main.data, i64 40, i1 false)
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #7
  %3 = getelementptr inbounds nuw i8, ptr %2, i64 4
  %4 = getelementptr inbounds nuw i8, ptr %2, i64 8
  %5 = getelementptr inbounds nuw i8, ptr %1, i64 32
  store i32 1, ptr %5, align 16, !tbaa !5
  %6 = getelementptr inbounds nuw i8, ptr %2, i64 12
  %7 = getelementptr inbounds nuw i8, ptr %2, i64 16
  %8 = getelementptr inbounds nuw i8, ptr %1, i64 36
  store i32 1, ptr %8, align 4, !tbaa !5
  %9 = getelementptr inbounds nuw i8, ptr %2, i64 20
  %10 = getelementptr inbounds nuw i8, ptr %2, i64 24
  %11 = getelementptr inbounds nuw i8, ptr %2, i64 28
  %12 = getelementptr inbounds nuw i8, ptr %1, i64 16
  %13 = getelementptr inbounds nuw i8, ptr %2, i64 32
  store <4 x i32> splat (i32 1), ptr %12, align 16, !tbaa !5
  %14 = getelementptr inbounds nuw i8, ptr %2, i64 36
  store <4 x i32> splat (i32 1), ptr %1, align 16, !tbaa !5
  br label %15

15:                                               ; preds = %0, %56
  %16 = phi i64 [ %59, %56 ], [ 0, %0 ]
  %17 = phi i32 [ %58, %56 ], [ 0, %0 ]
  %18 = getelementptr inbounds nuw i32, ptr %1, i64 %16
  %19 = load i32, ptr %18, align 4, !tbaa !5
  %20 = add nsw i32 %19, -1
  %21 = icmp sgt i32 %19, 0
  br i1 %21, label %22, label %56

22:                                               ; preds = %15
  %23 = sext i32 %17 to i64
  %24 = trunc nuw nsw i64 %16 to i32
  %25 = zext nneg i32 %19 to i64
  %26 = icmp ult i32 %19, 8
  br i1 %26, label %43, label %27

27:                                               ; preds = %22
  %28 = and i64 %25, 2147483640
  %29 = add nsw i64 %28, %23
  %30 = trunc nuw nsw i64 %28 to i32
  %31 = sub i32 %20, %30
  %32 = insertelement <4 x i32> poison, i32 %24, i64 0
  %33 = shufflevector <4 x i32> %32, <4 x i32> poison, <4 x i32> zeroinitializer
  %34 = getelementptr i32, ptr %2, i64 %23
  br label %35

35:                                               ; preds = %35, %27
  %36 = phi i64 [ 0, %27 ], [ %39, %35 ]
  %37 = getelementptr i32, ptr %34, i64 %36
  %38 = getelementptr inbounds nuw i8, ptr %37, i64 16
  store <4 x i32> %33, ptr %37, align 4, !tbaa !5
  store <4 x i32> %33, ptr %38, align 4, !tbaa !5
  %39 = add nuw i64 %36, 8
  %40 = icmp eq i64 %39, %28
  br i1 %40, label %41, label %35, !llvm.loop !18

41:                                               ; preds = %35
  %42 = icmp eq i64 %28, %25
  br i1 %42, label %53, label %43

43:                                               ; preds = %22, %41
  %44 = phi i64 [ %23, %22 ], [ %29, %41 ]
  %45 = phi i32 [ %20, %22 ], [ %31, %41 ]
  br label %46

46:                                               ; preds = %43, %46
  %47 = phi i64 [ %49, %46 ], [ %44, %43 ]
  %48 = phi i32 [ %51, %46 ], [ %45, %43 ]
  %49 = add nsw i64 %47, 1
  %50 = getelementptr inbounds i32, ptr %2, i64 %47
  store i32 %24, ptr %50, align 4, !tbaa !5
  %51 = add nsw i32 %48, -1
  %52 = icmp eq i32 %48, 0
  br i1 %52, label %53, label %46, !llvm.loop !19

53:                                               ; preds = %46, %41
  %54 = phi i64 [ %29, %41 ], [ %49, %46 ]
  %55 = trunc nsw i64 %54 to i32
  br label %56

56:                                               ; preds = %53, %15
  %57 = phi i32 [ %20, %15 ], [ -1, %53 ]
  %58 = phi i32 [ %17, %15 ], [ %55, %53 ]
  store i32 %57, ptr %18, align 4, !tbaa !5
  %59 = add nuw nsw i64 %16, 1
  %60 = icmp eq i64 %59, 10
  br i1 %60, label %61, label %15, !llvm.loop !17

61:                                               ; preds = %56
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #7
  %62 = load i32, ptr %2, align 16, !tbaa !5
  %63 = load i32, ptr %3, align 4, !tbaa !5
  %64 = icmp sgt i32 %62, %63
  br i1 %64, label %101, label %65

65:                                               ; preds = %61
  %66 = load i32, ptr %4, align 8, !tbaa !5
  %67 = icmp sgt i32 %63, %66
  br i1 %67, label %101, label %68

68:                                               ; preds = %65
  %69 = load i32, ptr %6, align 4, !tbaa !5
  %70 = icmp sgt i32 %66, %69
  br i1 %70, label %101, label %71

71:                                               ; preds = %68
  %72 = load i32, ptr %7, align 16, !tbaa !5
  %73 = icmp sgt i32 %69, %72
  br i1 %73, label %101, label %74

74:                                               ; preds = %71
  %75 = load i32, ptr %9, align 4, !tbaa !5
  %76 = icmp sgt i32 %72, %75
  br i1 %76, label %101, label %77

77:                                               ; preds = %74
  %78 = load i32, ptr %10, align 8, !tbaa !5
  %79 = icmp sgt i32 %75, %78
  br i1 %79, label %101, label %80

80:                                               ; preds = %77
  %81 = load i32, ptr %11, align 4, !tbaa !5
  %82 = icmp sgt i32 %78, %81
  br i1 %82, label %101, label %83

83:                                               ; preds = %80
  %84 = load i32, ptr %13, align 16, !tbaa !5
  %85 = icmp sgt i32 %81, %84
  br i1 %85, label %101, label %86

86:                                               ; preds = %83
  %87 = load i32, ptr %14, align 4, !tbaa !5
  %88 = icmp sgt i32 %84, %87
  br i1 %88, label %101, label %89

89:                                               ; preds = %86
  %90 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.1)
  %91 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %62, ptr noundef nonnull @.str.3)
  %92 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %63, ptr noundef nonnull @.str.3)
  %93 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %66, ptr noundef nonnull @.str.3)
  %94 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %69, ptr noundef nonnull @.str.3)
  %95 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %72, ptr noundef nonnull @.str.3)
  %96 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %75, ptr noundef nonnull @.str.3)
  %97 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %78, ptr noundef nonnull @.str.3)
  %98 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %81, ptr noundef nonnull @.str.3)
  %99 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %84, ptr noundef nonnull @.str.3)
  %100 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %87, ptr noundef nonnull @.str.4)
  br label %104

101:                                              ; preds = %86, %83, %80, %77, %74, %71, %68, %65, %61
  %102 = phi i32 [ 1, %61 ], [ 2, %65 ], [ 3, %68 ], [ 4, %71 ], [ 5, %74 ], [ 6, %77 ], [ 7, %80 ], [ 8, %83 ], [ 9, %86 ]
  %103 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %102)
  br label %104

104:                                              ; preds = %89, %101
  %105 = phi i32 [ 1, %101 ], [ 0, %89 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #7
  ret i32 %105
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i64(ptr noalias writeonly captures(none), ptr noalias readonly captures(none), i64, i1 immarg) #4

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #5

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write)
declare void @llvm.assume(i1 noundef) #6

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #3 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: readwrite) }
attributes #5 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #6 = { nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write) }
attributes #7 = { nounwind }

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
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.unroll.disable"}
!11 = distinct !{!11, !12}
!12 = !{!"llvm.loop.mustprogress"}
!13 = distinct !{!13, !12, !14, !15}
!14 = !{!"llvm.loop.isvectorized", i32 1}
!15 = !{!"llvm.loop.unroll.runtime.disable"}
!16 = distinct !{!16, !12, !15, !14}
!17 = distinct !{!17, !12}
!18 = distinct !{!18, !12, !14, !15}
!19 = distinct !{!19, !12, !15, !14}
